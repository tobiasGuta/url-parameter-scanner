import sys
import re
from tqdm import tqdm
import time

# List of URLs and patterns to search for (excluding numbers) (change it if needed)
parameters = [
    "?message=", "search?term=", "search?query=", "?name=", "?user=",
    "?id:", "?search:", "?page:", "?lang:", "?sort:",
    "?filter:", "?category:", "?view:", "?limit:", "?offset:",
    "?user:", "?theme:", "?token:", "?ref:", "?status:",
    "#section:", "#top:", "#comments:", "#footer:", "#tab:",
    "?ref:", "?tracking_id:", "?aff_id:", "?utm_source:", "?utm_medium:",
    "?utm_campaign:", "?discount:", "?token:", "?language:",
    "/id:", "/username:", "/post:", "/category:", "/product:",
    "/slug:", "/order:", "/group:", "/course:",
    "?action:", "?status:", "?sort_by:", "?page_size:", "?start_date:",
    "?end_date:", "?search_term:", "?filter_type:", "?order_by:", "?session_id:",
    "?device_id:", "?product_id:", "?view_mode:", "?user_role:", "?promo_code:"
    "/user_id:", "/profile:", "/comment_id:", "/article_id:", "/post_id:",
    "/tag:", "/category_id:", "/product_name:", "/cart_id:", "/wishlist_id:"
    "#related_posts:", "#comments_section:", "#pricing:", "#reviews:", "#contact_form:",
    "#map:", "#video_player:", "#faq:", "#terms_conditions:", "#disclaimer:"
    "?utm_term:", "?utm_content:", "?source:", "?medium:", "?campaign:",
    "?referral_code:", "?affiliate_id:", "?session_token:", "?discount_code:", "?tracking_code:"
    "?user_id:", "?session_token:", "?language_code:", "?location:", "?region:",
    "?device_type:", "?client_id:", "?response_format:", "?source_page:", "?referrer_url:",
    "?event_id:", "?transaction_id:", "?product_type:", "?discount_type:", "?coupon_code:",
    "?promo_id:", "?discount_percent:", "?order_status:", "?payment_status:", "?method:"
    "/product_category:", "/user_profile:", "/transaction/", "/order_history:", "/address_book:",
    "/order_summary:", "/checkout/", "/cart/", "/payment_method:", "/customer_feedback:",
    "/support_ticket:", "/ticket_id:", "/order_tracking:", "/purchase_history:", "/delivery_info:"
    "#error_section:", "#success_message:", "#checkout_summary:", "#login_form:", "#signup_form:",
    "#login_modal:", "#order_details:", "#cart_items:", "#address_form:", "#shipping_info:"
    "?source_url:", "?aff_link:", "?campaign_id:", "?ad_group_id:", "?utm_referral:",
    "?utm_content:", "?referral_partner:", "?device_platform:", "?offer_code:", "?reward_points:"
    "?action_type:", "?filter_by:", "?sub_category:", "?user_type:", "?auth_token:",
    "?category_filter:", "?page_count:", "?keyword:", "?start_time:", "?end_time:",
    "?transaction_type:", "?country_code:", "?zip_code:", "?delivery_type:", "?payment_method:",
    "?discount_value:", "?shipping_method:", "?date_range:", "?product_variant:", "?sort_field:",
    "?date_added:", "?account_status:", "?cart_total:", "?brand_filter:", "?stock_status:"
    "/subscription_status:", "/payment_history:", "/order_update/", "/shipment_status:", "/inventory/",
    "/user_activity:", "/billing_info:", "/purchase_details:", "/payment_info:", "/subscription_id:",
    "/event_detail:", "/order_review:", "/order_confirmation:", "/user_feedback:", "/order_cancel/",
    "/wishlist_items:", "/favorite_products:", "/address_details:", "/product_reviews:"
    "#sign_in_form:", "#sign_up_form:", "#reset_password:", "#product_specifications:", "#order_summary:",
    "#payment_options:", "#shipping_details:", "#order_tracking_info:", "#product_details:", "#subscription_options:"
    "?lead_source:", "?utm_id:", "?media_source:", "?placement_id:", "?campaign_tag:",
    "?creative_id:", "?affiliate_campaign:", "?referrer_id:", "?ad_type:", "?tracking_partner:",
    "?influencer_id:", "?reward_code:", "?coupon_code_type:", "?source_type:", "?utm_campaign_id:",
    "?referral_source:", "?discount_percentage:", "?promo_type:", "?session_duration:"
    "?search_query:", "?item_id:", "?page_number:", "?language_preference:", "?currency:",
    "?affiliate_code:", "?transaction_status:", "?payment_status:", "?product_category:", "?user_group:",
    "?user_status:", "?geo_location:", "?device_info:", "?session_id:", "?event_code:",
    "?offer_id:", "?discount_code:", "?gift_card:", "?invoice_id:", "?order_date:", "?delivery_date:",
    "?return_code:", "?order_reference:", "?shipping_zip:", "?promo_code_type:", "?discount_type:",
    "?search_filter:", "?priority_level:", "?error_code:", "?error_message:", "?user_feedback:"
    "/account_settings:", "/order_update/", "/user_details/", "/order_history/", "/payment_details/",
    "/user_dashboard:", "/transaction_details:", "/order_invoice:", "/product_details/", "/wishlist/",
    "/order_review:", "/product_reviews:", "/cart_summary:", "/shipping_address:", "/product_search/",
    "/order_complete:", "/subscription_plan:", "/payment_method_choice:", "/tracking_info/",
    "/membership_plan:", "/discounts/", "/reward_points/", "/user_notifications:", "/product_type:"
    "#checkout_review:", "#product_overview:", "#user_preferences:", "#user_profile:", "#order_history:",
    "#shipping_options:", "#payment_options:", "#order_review:", "#error_message:", "#welcome_message:",
    "#user_rating:", "#faq_section:", "#return_policy:", "#terms_of_service:", "#site_map:"
    "?utm_source_id:", "?utm_medium_id:", "?utm_campaign_id:", "?referral_code_id:", "?tracking_id_v2:",
    "?influencer_campaign:", "?ad_source:", "?affiliate_partners:", "?source_campaign:", "?session_duration:",
    "?user_engagement:", "?ad_position:", "?ad_format:", "?ad_id:", "?media_channel:", "?ad_performance:",
    "?email_campaign:", "?customer_segment:", "?referral_partner_id:", "?promo_type_id:", "?transaction_value:"
    "?api_key:", "?user_token:", "?session_token:", "?app_version:", "?auth_code:",
    "?app_id:", "?referrer_id:", "?page_size_limit:", "?max_results:", "?start_date_range:",
    "?end_date_range:", "?search_type:", "?error_type:", "?error_details:", "?external_id:",
    "?response_code:", "?result_count:", "?action_status:", "?retry_count:", "?retry_time:",
    "?confirmation_code:", "?approval_status:", "?request_id:", "?callback_url:", "?locale:",
    "?timezone:", "?ip_address:", "?device_platform:", "?user_agent:", "?os_version:"
    "/login/", "/signup/", "/logout/", "/reset_password/", "/email_verification/",
    "/user_activation/", "/transaction_summary/", "/product_details/", "/order_tracking/",
    "/payment_confirmation/", "/product_listing/", "/search_results/", "/checkout_form/",
    "/payment_page/", "/profile_picture/", "/account_security/", "/password_change/",
    "/user_orders/", "/product_reviews/", "/subscription_management/", "/plan_upgrade/",
    "/account_deletion/", "/purchase_history/", "/order_invoice/", "/support_ticket/", "/order_refund/"
    "#order_confirmation:", "#address_form:", "#tracking_section:", "#user_dashboard:", "#newsletter_signup:",
    "#profile_settings:", "#review_section:", "#delivery_information:", "#privacy_policy:", "#cookie_notice:",
    "#error_modal:", "#sign_in_modal:", "#terms_conditions:", "#payment_options:", "#support_center:"
    "?ref_code:", "?referrer_token:", "?click_id:", "?sub_campaign_id:", "?utm_partner:",
    "?influencer_token:", "?creative_token:", "?ad_placement_id:", "?content_type:", "?media_source_id:",
    "?ad_group_id:", "?click_through_rate:", "?conversion_rate:", "?roi:", "?user_engagement_id:",
    "?transaction_tag:", "?product_category_id:", "?promotion_type_id:", "?campaign_source_id:",
    "?discount_amount:", "?coupon_code_value:", "?purchase_source:", "?social_media_campaign:"
    "?token_id:", "?api_version:", "?user_auth_token:", "?account_number:", "?referral_code:",
    "?registration_key:", "?status_code:", "?event_timestamp:", "?discount_code_value:", "?payment_status_id:",
    "?order_id:", "?product_code:", "?order_status_id:", "?delivery_status:", "?user_type_id:",
    "?subscription_status:", "?login_status:", "?group_id:", "?campaign_code:", "?plan_id:",
    "?subscription_id:", "?transaction_token:", "?currency_code:", "?shipping_address_id:", "?coupon_percentage:",
    "?payment_method_id:", "?product_quantity:", "?tracking_id_value:", "?user_login:", "?user_account_type:"
    "/order_summary/", "/product_search/", "/payment_success/", "/checkout_confirmation/",
    "/cart_review/", "/user_dashboard/", "/shipping_details/", "/order_confirmation/", "/payment_method_selection/",
    "/order_tracking/", "/transaction_history/", "/user_profile/", "/update_preferences/", "/subscription_details/",
    "/plan_details/", "/order_details/", "/user_support/", "/account_settings/", "/order_refund/",
    "/product_reviews/", "/cart_addition/", "/product_wishlist/", "/order_processing/", "/address_update/"
    "#cart_summary:", "#delivery_info:", "#payment_options:", "#order_overview:", "#user_account_info:",
    "#wishlist_details:", "#billing_info:", "#order_updates:", "#error_feedback:", "#thank_you_message:",
    "#shipping_options:", "#order_confirmation_modal:", "#login_form:", "#help_center:", "#terms_of_use:"
    "?source_id:", "?media_id:", "?campaign_name:", "?promotion_code:", "?partner_id:",
    "?referral_partner:", "?session_ref:", "?source_platform:", "?source_channel:", "?purchase_source_id:",
    "?affiliate_id:", "?referral_source_code:", "?tracking_pixel_id:", "?user_activity_id:", "?site_referrer:",
    "?tracking_campaign_id:", "?event_type:", "?ad_group_name:", "?ad_campaign_id:", "?click_through_id:",
    "?utm_campaign_token:", "?influencer_link_id:", "?content_partner:", "?media_channel_id:", "?conversion_source:"
]

# Function to search for specific parameters in a text file and show the full matching URL
def search_parameters(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()

            print("\n🔍 Searching for parameters in the file...\n")
            time.sleep(0.5)  # Pause to simulate animation start

            found_count = 0
            found_urls = {}

            # Adjusting tqdm parameters for better display
            for line in tqdm(content, desc="Scanning lines", unit="line", colour="cyan", ncols=100, mininterval=0.1):
                url = line.strip()
                for param in parameters:
                    if param in url:
                        # Extract URL up to the parameter to track uniqueness
                        base_url = url.split(param)[0]
                        param_url_combo = f"{base_url}{param}"

                        # Avoid printing the same URL and parameter combination more than once
                        if param_url_combo not in found_urls:
                            found_urls[param_url_combo] = True
                            time.sleep(0.05)  # Slight delay for each found parameter
                            found_count += 1
                            tqdm.write(f"👍 Found parameter: {url}")

            if found_count == 0:
                tqdm.write("\nNo parameters found in the file.")
            else:
                tqdm.write(f"\n🎉 Total parameters found: {found_count}")

    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python param.py <file_path>")
    else:
        search_parameters(sys.argv[1])
