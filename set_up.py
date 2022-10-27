null = None

def api_config(account_id, start_date, end_date, currency_id, conv_tags_ids):
  APIObject = {
      "entities": [{
          "type": "AnalyticsReport",
          "reportName": "test",
          "reportScope": {
              "entitiesHierarchy": {
                  "entitiesHierarchyLevelType": "ACCOUNT",
                  "accountContext": account_id,
                  "accounts": [account_id],
                  "advertisers": [],
                  "sites": [],
                  "campaignsType": ["Display"]
              },
              "attributionModelID": -1,
              "impressionCookieWindow": 0,
              "clickCookieWindow": 0,
              "filters": {
                "conversionTagIDs": conv_tags_ids
              },
              "currencyOptions": {
                  "type": "Custom",
                  "defaultCurrency": currency_id,
                  "targetCurrency": currency_id,
                  "currencyExchangeDate": end_date
              },
              "timeRange": {
                  "timeZone": "US/Eastern",
                  "type": "Custom",
                  "dataStartTimestamp": f"{start_date}T04:00:00.000Z",
                  "dataEndTimestamp": f"{end_date}T03:59:59.999Z"
              },
              "presetId": null
          },
          "reportStructure": {
          "attributeIDs": [
            "Account ID",
            "Advertiser ID",
            "Account Name",
            "Advertiser Name",
            "Campaign Name",
            "Campaign ID",
            "Package Name",
            "Package ID",
            "Placement Name",
            "Placement ID",
            "Ad Name",
            "Ad ID",
            "Site Name",
            "Site ID"
          ],
          "metricIDs": [
            "Total Clicks",
            "Served Impressions",
            "Video Started",
            "Video Played 75%",
            "Video Fully Played",
            "Total Conversions",
            "Total Media Cost"
          ],
              "attributeIDsOnColumns": [
                "Conversion Tag Name"
              ],
              "timeBreakdown": "Day"
          },
          "reportExecution": {
              "type": "Ad_Hoc"
          },
          "reportDeliveryMethods": [{
              "type": "URL",
              "exportFileType": "JSON",
              "compressionType": "NONE",
              "emailRecipients": ["email@test.com"],
              "exportFileNamePrefix": f"{account_id}_{start_date}_{end_date}"
          }],
          "reportAuthorization": {
              "type": "mm3",
              "userID": 1234 
          }
      }]
  }
  return APIObject