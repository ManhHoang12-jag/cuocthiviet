import streamlit as st

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Cuộc thi VHNT Lai Châu 2026", page_icon="🏔️", layout="wide")

# --- 2. TÙY CHỈNH GIAO DIỆN CHUYÊN NGHIỆP VÀ TĂNG CỠ CHỮ (CSS) ---
st.markdown("""
    <style>
    /* XÓA BỎ HOÀN TOÀN TẤT CẢ LOGO, MENU, THANH TRANG TRÍ VÀ NÚT DEPLOY CỦA STREAMLIT
       Giúp giao diện website thuần khiết, trang trọng như một trang báo điện tử chính thống.
    */
    header, [data-testid="stHeader"], 
    footer, 
    [data-testid="stMainMenu"], 
    [data-testid="stDecoration"], 
    [data-testid="stStatusWidget"], 
    .stDeployButton {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* KHỬ TRIỆT ĐỂ KHOẢNG TRẮNG THỪA Ở ĐẦU TRANG (ĐÃ ÉP XUỐNG 0REM TUYỆT ĐỐI)
       Quét sạch khoảng trống của cả lớp cũ lẫn lớp cấu trúc mới trong Streamlit
    */
    div[data-testid="stAppViewContainer"] .main .block-container,
    [data-testid="stMainBlockContainer"] {
        padding-top: 0rem !important;
        margin-top: 0px !important;
    }
    
    /* Cấu hình font chữ hệ thống hiện đại, dễ đọc và tăng cỡ chữ cơ bản */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
    }
    
    /* Tăng cỡ chữ và kéo giãn dòng cho toàn bộ văn bản thường */
    .stMarkdown p, .stText, [data-testid="stMarkdownContainer"] p {
        font-size: 17px !important;
        line-height: 1.65 !important;
        color: #2d3748 !important;
    }
    
    /* Tăng cỡ chữ cho danh sách gạch đầu dòng */
    .stMarkdown li {
        font-size: 17px !important;
        line-height: 1.65 !important;
        margin-bottom: 8px;
    }
    
    /* Phóng to và định dạng lại các khối tiêu đề mục lớn */
    .tieu-de-muc {
        background-color: #003366;
        color: white;
        padding: 12px 18px;
        font-weight: bold;
        font-size: 20px; /* Tăng cỡ chữ tiêu đề mục */
        border-radius: 4px;
        margin-top: 25px;
        margin-bottom: 15px;
        border-left: 6px solid #b22222;
    }
    
    /* Định dạng tăng kích thước các hộp giải thưởng */
    .box-giaithuong {
        background-color: #ffffff; 
        padding: 18px; 
        border-radius: 10px;
        border-top: 5px solid #d4af37; 
        box-shadow: 2px 2px 8px rgba(0,0,0,0.08); 
        text-align: center;
    }
    
    /* Tùy chỉnh tăng kích thước chữ và độ đậm cho các nút liên kết bài viết */
    div.stButton > button {
        font-size: 17px !important;
        font-weight: bold !important;
        text-align: left !important;
        line-height: 1.4 !important;
        color: #003366 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. KHỞI TẠO CÁC TRẠNG THÁI HỆ THỐNG (SESSION STATE) ---
if "bai_viet_hien_tai" not in st.session_state:
    st.session_state.bai_viet_hien_tai = None

# Kho dữ liệu bài viết tin tức
CSDL_BAI_VIET = {
    "tin_chinh": {
        "tieu_de": 'Lễ phát động Cuộc thi sáng tác các tác phẩm văn học nghệ thuật viết về Lai Châu "Lai Châu - Mạch nguồn văn hóa, tiềm năng, động lực phát triển"',
        "noi_dung": """Sáng nay, Ban Tổ chức đã chính thức phát động cuộc thi nhằm khơi dậy nguồn cảm hứng sáng tác, tôn vinh vẻ đẹp thiên nhiên, con người và bản sắc văn hóa các dân tộc tỉnh Lai Châu. 
        
        Tham dự lễ phát động có đại diện lãnh đạo Tỉnh ủy, Ban Tuyên giáo, Hội Văn học Nghệ thuật tỉnh cùng đông đảo các văn nghệ sĩ, phóng viên báo chí trung ương và địa phương. Cuộc thi được kỳ vọng sẽ tìm kiếm được nhiều tác phẩm đỉnh cao, phản ánh chân thực khát vọng vươn lên, tiềm năng và động lực phát triển của tỉnh trong thời kỳ đổi mới."""
    },
    "tin_phu_1": {
        "tieu_de": "Hướng dẫn chi tiết cách thức gửi bài dự thi trực tuyến đạt chuẩn.",
        "noi_dung": "Các tác giả lưu ý khi gửi bài qua Email cá nhân cần đính kèm file định dạng .docx hoặc PDF. Nội dung thư phải ghi đầy đủ thông tin liên hệ theo đúng biểu mẫu hướng dẫn tại mục Gửi bài dự thi ở cuối trang chủ. Vui lòng không nén file quá nặng hoặc gửi link hỏng."
    },
    "tin_phu_2": {
        "tieu_de": "Phát động các tác giả thâm nhập thực tế tại các xã biên giới.",
        "noi_dung": "Ban Tổ chức dự kiến phối hợp tổ chức các chuyến đi thâm nhập thực tế tại các xã biên giới, vùng sâu vùng xa trên địa bàn tỉnh Lai Châu nhằm hỗ trợ tạo nguồn tư liệu chân thực, sinh động cho các văn nghệ sĩ tìm kiếm chất liệu sáng tác sâu sát with đời sống bà con đồng bào dân tộc."
    },
}

# --- 4. HEADER: BANNER ĐẦU TRANG ---
try:
    st.image("banner.jpg", use_container_width=True)
except FileNotFoundError:
    st.warning("📌 Khu vực hiển thị Banner: Đang chờ cập nhật file 'banner.jpg' vào thư mục.")

st.write("")

# ==========================================
# PHẦN 5: XỬ LÝ ĐIỀU HƯỚNG HIỂN THỊ TRANG
# ==========================================

# TÌNH HUỐNG A: XEM CHI TIẾT BÀI VIẾT (Mở rộng toàn trang, chữ lớn)
if st.session_state.bai_viet_hien_tai is not None:
    ma_bai = st.session_state.bai_viet_hien_tai
    bai_viet = CSDL_BAI_VIET[ma_bai]
    
    if st.button("⬅ QUAY LẠI TRANG CHỦ"):
        st.session_state.bai_viet_hien_tai = None
        st.rerun()
        
    st.write("")
    st.markdown(f"<h2 style='color: #003366; font-weight: bold; font-size: 25px;'>{bai_viet['tieu_de']}</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 10px 0; border-color: #b22222; border-width: 2px;'>", unsafe_allow_html=True)
    
    if ma_bai == "tin_chinh":
        st.image("anh_khai_mac.jpg", use_container_width=True)
        
    # ĐÃ ĐỔI SANG THỂ HTML CÓ PRE-WRAP ĐỂ GIỮ NGUYÊN TOÀN BỘ CÁC DẤU XUỐNG DÒNG CỦA BÀI VIẾT
    st.markdown(f"""
        <div style="white-space: pre-wrap; font-size: 17px; line-height: 1.65; color: #2d3748;">
            {bai_viet['noi_dung']}
        </div>
    """, unsafe_allow_html=True)
    st.write("")

# TÌNH HUỐNG B: TRANG CHỦ CHÍNH BỐ CỤC SONG SONG ĐỐI XỨNG (50% - 50%)
else:
    col_left, col_right = st.columns([5, 5])
    
    # ---------------------------------------------------------
    # CỘT BÊN TRÁI (Tin tức, Văn bản, Hướng dẫn gửi bài)
    # ---------------------------------------------------------
    with col_left:
        
        # MỤC 1: TIN TỨC HOẠT ĐỘNG
        st.markdown("""
        <div style="background-color: #b22222; color: white; padding: 10px 15px; font-weight: bold; font-size: 18px; margin-bottom: 15px; border-radius: 4px;">
            <span style="margin-right: 5px;">📰</span> TIN TỨC HOẠT ĐỘNG
        </div>
        """, unsafe_allow_html=True)
        
        st.image("anh_khai_mac.jpg", use_container_width=True)
        
        if st.button(CSDL_BAI_VIET["tin_chinh"]["tieu_de"], key="btn_tin_chinh"):
            st.session_state.bai_viet_hien_tai = "tin_chinh"
            st.rerun()
            
        st.write("Sáng nay, ngày 02/6 Ban Tổ chức cuộc thi đã chính thức phát động cuộc thi nhằm khơi dậy nguồn cảm hứng sáng tác, tôn vinh vẻ đẹp thiên nhiên, con người và bản sắc văn hóa các dân tộc tỉnh Lai Châu...")
        
        st.markdown("<p style='font-weight:bold; color:#555; margin-top:15px; margin-bottom:5px; font-size:17px;'>CÁC TIN KHÁC:</p>", unsafe_allow_html=True)
        if st.button(f"■ {CSDL_BAI_VIET['tin_phu_1']['tieu_de']}", key="btn_tp1"):
            st.session_state.bai_viet_hien_tai = "tin_phu_1"
            st.rerun()
        if st.button(f"■ {CSDL_BAI_VIET['tin_phu_2']['tieu_de']}", key="btn_tp2"):
            st.session_state.bai_viet_hien_tai = "tin_phu_2"
            st.rerun()

        # MỤC 2: VĂN BẢN CHỈ ĐẠO & TÀI LIỆU (Đã cập nhật cấu trúc 3 cột kèm mã QR)
        st.markdown("<div class='tieu-de-muc'>📜 VĂN BẢN CHỈ ĐẠO & TÀI LIỆU CUỘC THI</div>", unsafe_allow_html=True)
        col_vb1, col_vb2, col_vb3 = st.columns([3.5, 3.5, 3])
        
        with col_vb1:
            st.subheader("1. Thể lệ cuộc thi")
            st.link_button(
                label="📥 Xem & Tải Thể lệ (PDF)", 
                url="https://drive.google.com/file/d/1FhYDCGM6QW8ZgSu4F4Qnlm3GYNO0i3WC/view?usp=drive_link", 
                use_container_width=True
            )
            
        with col_vb2:
            st.subheader("2. Kế hoạch tổ chức")
            st.link_button(
                label="📥 Xem & Tải Kế hoạch (PDF)", 
                url="https://drive.google.com/file/d/1kbL1zyun3czW1xcOkQPU-_m_Nk4kozHh/view?usp=drive_link", 
                use_container_width=True
            )
            
        with col_vb3:
            st.subheader("3. Mã QR tài liệu")
            try:
                st.image("qr_tailieu.jpg", use_container_width=True)
            except FileNotFoundError:
                st.warning("📌 Thiếu file 'qr_tailieu.jpg'.")

        # MỤC 3: HƯỚNG DẪN GỬI BÀI DỰ THI
        st.markdown("<div class='tieu-de-muc'>📩 HƯỚNG DẪN GỬI TÁC PHẨM DỰ THI</div>", unsafe_allow_html=True)
        st.markdown("""
        <div style="background-color: #ffffff; padding: 18px; border-radius: 8px; border-left: 5px solid #b22222; box-shadow: 2px 2px 6px rgba(0,0,0,0.05); margin-bottom: 15px;">
            <p style="color: #003366; font-weight: bold; margin-bottom: 4px; font-size: 18px;">HỘP THƯ TIẾP NHẬN CHÍNH THỨC:</p>
            <p style="color: #b22222; font-weight: bold; font-size: 20px; margin-bottom: 4px;">cuocthivietvelaichau@gmail.com</p>
            <p style="color: #64748b; font-size: 15px; margin-bottom: 0; line-height: 1.45;">
                Ban Tuyên giáo và Dân vận Tỉnh ủy Lai Châu - Tầng 7, Nhà A, Trung tâm Hành chính - Chính trị tỉnh, phường Tân Phong, tỉnh Lai Châu.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.info("**📌 Tiêu đề Email:** `[Dự thi VHNT Lai Châu] - Thể loại - Tên tác phẩm - Họ tên tác giả` \n\n **📋 Ví dụ:** Dự thi VHNT Lai Châu - Truyện ngắn - Mùa hoa cà - Nguyễn Văn A.")

    # ---------------------------------------------------------
    # CỘT BÊN PHẢI (Video, Thư viện ảnh Native, Lộ trình, Giải thưởng)
    # ---------------------------------------------------------
    with col_right:
        
        # MỤC 1: VIDEO GIỚI THIỆU
        st.markdown("""
        <div style="background-color: #003366; color: white; padding: 10px 15px; font-weight: bold; font-size: 18px; margin-bottom: 15px; border-radius: 4px;">
            <span style="margin-right: 5px;">🎥</span> VIDEO GIỚI THIỆU LAI CHÂU
        </div>
        """, unsafe_allow_html=True)
        st.video("https://youtu.be/SvYvffwAvYY")

        # MỤC 2: THƯ VIỆN HÌNH ẢNH NATIVE CHỐNG SẬP ĐIỆN THOẠI 100%
        st.markdown("<div class='tieu-de-muc'>📸 THƯ VIỆN HÌNH ẢNH GỢI CẢM HỨNG</div>", unsafe_allow_html=True)
        
        tab_anh, tab_clip = st.tabs(["Thư viện ảnh", "Clip Tư liệu"])
        
        with tab_anh:
            so_luong_anh = 12  # Đặt số lượng ảnh thực tế của anh (12 hoặc 20 ảnh đều chạy mượt)
            
            # Sử dụng hệ thống cột native của Streamlit để xếp ảnh vuông vắn, siêu nhẹ
            # Duyệt qua danh sách, mỗi hàng hiển thị 3 ảnh song song trên máy tính
            for i in range(1, so_luong_anh + 1, 3):
                cols = st.columns(3)
                for idx, col in enumerate(cols):
                    if i + idx <= so_luong_anh:
                        with col:
                            try:
                                st.image(f"thuvien_{i+idx}.jpg", use_container_width=True)
                            except FileNotFoundError:
                                # Ảnh dự phòng nếu thiếu file cục bộ
                                st.image("http://googleusercontent.com/image_collection/image_retrieval/3705218641779458257", use_container_width=True)

        with tab_clip:
            st.subheader("Phóng sự tư liệu phát động sáng tác")
            st.video("https://youtu.be/SvYvffwAvYY")

        # MỤC 3: LỘ TRÌNH TỔ CHỨC
        st.markdown("<div class='tieu-de-muc'>📅 THỜI GIAN</div>", unsafe_allow_html=True)
        st.markdown("• **Phát động cuộc thi:** Tháng 06/2026 \n\n • **Hạn chót tiếp nhận tác phẩm:** Hết ngày 15/09/2026 \n\n • **Tổng kết và Lễ Trao giải:** Trong tháng 10/2026")

        # MỤC 4: CƠ CẤU GIẢI THƯỞNG
        st.markdown("<div class='tieu-de-muc'>🏆 CƠ CẤU GIẢI THƯỞNG</div>", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown('<div class="box-giaithuong"><b style="font-size:15px;">01 Giải Nhất</b><h3 style="color:#b22222; margin:5px 0; font-size:20px;">7 Triệu đồng</h3></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="box-giaithuong"><b style="font-size:15px;">02 Giải Nhì</b><h3 style="color:#b22222; margin:5px 0; font-size:20px;">Mỗi giải 5 Triệu đồng</h3></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="box-giaithuong"><b style="font-size:15px;">04 Giải Ba</b><h3 style="color:#b22222; margin:5px 0; font-size:20px;">Mỗi giải 3.5 Triệu đồng</h3></div>', unsafe_allow_html=True)
        with c4: st.markdown('<div class="box-giaithuong"><b style="font-size:15px;">06 Giải KK</b><h3 style="color:#b22222; margin:5px 0; font-size:20px;"> Mỗi giải 2.1 Triệu đồng</h3></div>', unsafe_allow_html=True)

# --- 6. CHÂN TRANG (FOOTER) ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color: #64748b; font-size: 15px;'>© 2026 Ban Tổ chức Cuộc thi - Tỉnh ủy Lai Châu</p>", unsafe_allow_html=True)
