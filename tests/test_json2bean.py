import unittest
# how to import json2bean.py
import handy_tool.json2bean as j2


class TestJson2Bean(unittest.TestCase):
    json_data = """{
      "account_id": 11683,
      "is_employee": false,
      "last_modified_date": 1617801000,
      "last_access_date": 1617824890,
      "reputation_change_year": 19796,
      "reputation_change_quarter": 1430,
      "reputation_change_month": 1430,
      "reputation_change_week": 810,
      "reputation_change_day": 195,
      "reputation": 1250548,
      "creation_date": 1222430705,
      "user_type": "registered",
      "user_id": 22656,
      "accept_rate": 86,
      "location": "Reading, United Kingdom",
      "website_url": "http://csharpindepth.com",
      "link": "https://stackoverflow.com/users/22656/jon-skeet",
      "profile_image": "https://www.gravatar.com/avatar/6d8ebb117e8d83d74ea95fbdd0f87e13?s=128&d=identicon&r=PG",
      "display_name": "Jon Skeet"
    }"""

    def test_run(self):
      pass
      # print(j2.parser_java("test", self.json_data))

    def test_1(self):
      json_str = """
      {
        "id": "20200901135301233-000036ncThX7NP",
        "categoryId": "20191217165657971-0000015c4MFng6",
        "categoryName": "气眼",
        "categoryLinkName": [
          "五金",
          "气眼"
        ],
        "name": "五金商品",
        "code": "FWJ200900001",
        "image": "https://smebimage.fuliaoyi.com/FsOdMCzEGnLvmWawt3cmUcmz02ts",
        "images": null,
        "state": 2,
        "stateMessage": "可售卖",
        "sourceType": 1,
        "sourceTypeMessage": "非询价商品",
        "itemCount": 4,
        "minPrice": 1,
        "maxPrice": 1
      }
      """
      print(j2.parser_java("Test", json_str))

    def test_inner(self):
      json_data = """
      {
        "a": {
          "b": 1
        },
        "b": 2,
        "c": [1, 2, 3]
      }
      """
      print(j2.parser_java("test", json_data))


if __name__ == '__main__':
    unittest.main()