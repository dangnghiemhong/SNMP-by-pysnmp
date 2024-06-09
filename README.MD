# Công cụ Giám sát Mạng SNMP với Giao diện Đồ họa (GUI)

## Giới thiệu

Dự án này cung cấp một công cụ tiện lợi và dễ sử dụng để giám sát và quản lý các thiết bị mạng thông qua giao thức SNMP (Simple Network Management Protocol). Với giao diện đồ họa trực quan (GUI) được xây dựng bằng Tkinter, công cụ giúp đơn giản hóa việc tương tác với các thiết bị mạng và thu thập thông tin quan trọng về trạng thái hoạt động của chúng.

## Tính năng chính

* **Truy vấn thông tin thiết bị:** Lấy thông tin chi tiết từ một thiết bị mạng cụ thể (IP address) bằng cách sử dụng SNMP GET. Các thông tin cơ bản như thời gian hoạt động, thông tin liên hệ, tên thiết bị, vị trí, mô tả hệ thống, số lượng tiến trình và dung lượng RAM sẽ được hiển thị.

* **Quét mạng:** Khám phá và liệt kê các thiết bị SNMP có trong một mạng con (subnet) nhất định. Tính năng này giúp bạn nhanh chóng xác định các thiết bị hoạt động trên mạng và thu thập thông tin cơ bản về chúng như tên thiết bị.

* **Truy vấn OID tùy chỉnh:** Lấy giá trị của một OID (Object Identifier) cụ thể từ một thiết bị mạng. Điều này cho phép bạn truy cập vào các thông tin chi tiết hơn về thiết bị, tùy thuộc vào MIB (Management Information Base) mà thiết bị hỗ trợ.

## Yêu cầu hệ thống

* **Python 3.x:** Đảm bảo bạn đã cài đặt Python phiên bản 3.x trên hệ thống của mình.
* **Thư viện PySNMP:** Cài đặt thư viện PySNMP để làm việc với giao thức SNMP. Bạn có thể cài đặt bằng lệnh `pip install pysnmp`.
* **Thư viện ipaddress:** Thư viện này thường đã có sẵn trong Python, dùng để làm việc với các địa chỉ IP và mạng con.
* **Thư viện Tkinter:** Thư viện này cũng thường đã có sẵn trong Python, dùng để xây dựng giao diện đồ họa (GUI).

## Cài đặt và sử dụng

1. **Cài đặt:**
   * Mở terminal hoặc command prompt.
   * Chạy lệnh `pip install pysnmp` để cài đặt thư viện PySNMP.

2. **Tải mã nguồn:**
   * Sao chép hoặc tải mã nguồn từ kho lưu trữ về máy tính của bạn.

3. **Chạy chương trình:**
   * Mở terminal hoặc command prompt.
   * Điều hướng đến thư mục chứa mã nguồn.
   * Chạy lệnh `python main.py` (hoặc tên file tương ứng).

4. **Giao diện đồ họa:**
   * Chọn một trong các chức năng: "Get", "Scan Network" hoặc "Get Single OID".
   * Nhập các thông tin cần thiết vào các ô tương ứng.
   * Nhấn nút "Send" để thực hiện truy vấn.
   * Kết quả sẽ được hiển thị trong cửa sổ dòng lệnh.

5. **Dòng lệnh:**
   * Nếu bạn muốn sử dụng giao diện dòng lệnh, hãy chọn "no" khi được hỏi về việc sử dụng GUI.
   * Làm theo hướng dẫn trên dòng lệnh để chọn chức năng và nhập thông tin.

## Cấu trúc dự án

* `main.py`: Chứa mã nguồn chính, xử lý giao diện GUI và các chức năng chính của chương trình.
* `SnmpOperations.py`: Chứa các hàm để thực hiện các thao tác SNMP như `get`, `getsingleoid`.

## Lưu ý

* **SNMPv1/v2c:** Hiện tại, công cụ chỉ hỗ trợ các phiên bản SNMPv1 và SNMPv2c, sử dụng community string để xác thực.
* **Xử lý lỗi:** Chương trình có xử lý một số lỗi cơ bản. Tuy nhiên, việc xử lý lỗi có thể được cải thiện thêm để đảm bảo tính ổn định và đáng tin cậy.
* **Bảo mật:** Khi sử dụng SNMP, hãy cẩn thận với việc bảo mật thông tin xác thực (community string).

## Tương lai

* **SNMPv3:** Hỗ trợ thêm giao thức SNMPv3 để tăng cường bảo mật.
* **Cải thiện GUI:** Thiết kế giao diện thân thiện và trực quan hơn, có thể hiển thị kết quả trong bảng hoặc biểu đồ.
* **Ghi log:** Thêm tính năng ghi log để theo dõi các hoạt động và lỗi.
* **Tùy biến:** Cho phép người dùng tùy chỉnh các OID được truy vấn.

## Đóng góp

Mọi đóng góp đều được hoan nghênh! Nếu bạn có ý tưởng cải tiến hoặc sửa lỗi, xin vui lòng tạo một pull request.

