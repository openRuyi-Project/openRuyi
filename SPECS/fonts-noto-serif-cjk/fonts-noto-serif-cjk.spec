# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-noto-serif-cjk
Version:        2.003
Release:        %autorelease
Summary:        Noto Serif CJK Font Families
License:        OFL-1.1
URL:            https://notofonts.github.io/
VCS:            git:https://github.com/notofonts/noto-cjk
#!RemoteAsset
Source0:        https://github.com/notofonts/noto-cjk/releases/download/Serif%{version}/02_NotoSerifCJK-OTF-VF.zip
#!RemoteAsset
Source1:        https://github.com/notofonts/noto-cjk/releases/download/Serif%{version}/04_NotoSerifCJKOTC.zip
BuildArch:      noarch

BuildRequires:  unzip

# By default, we only install the variable fonts
Requires:       %{name}-vf = %{version}-%{release}

%description
Noto is a collection of high-quality fonts with multiple weights and widths in sans,
serif, mono, and other styles, in more than 1,000 languages and over 150 writing systems.

This package contains Noto Serif CJK fonts.

%package        vf
Summary:        Variable fonts in Noto Serif CJK font families

%description    vf
Noto is a collection of high-quality fonts with multiple weights and widths in sans,
serif, mono, and other styles, in more than 1,000 languages and over 150 writing systems.

This package contains Noto Serif CJK variable fonts for variable font support.

%package        static
Summary:        Static fonts in Noto Serif CJK font families

%description    static
Noto is a collection of high-quality fonts with multiple weights and widths in sans,
serif, mono, and other styles, in more than 1,000 languages and over 150 writing systems.

This package contains Noto Serif CJK static fonts for static font support.

%prep
%autosetup -c -a 1

%build
# No build required

%install
# Install vf fonts
mkdir -p %{buildroot}%{_datadir}/fonts/opentype
cp Variable/OTF/NotoSerifCJK*-VF.?tf %{buildroot}%{_datadir}/fonts/opentype

# Install static fonts
mkdir -p %{buildroot}%{_datadir}/fonts/truetype
cp OTC/NotoSerifCJK-*.ttc %{buildroot}%{_datadir}/fonts/truetype

%files

%files vf
%license LICENSE
%{_datadir}/fonts/opentype/NotoSerifCJK*-VF.?tf

%files static
%license LICENSE
%{_datadir}/fonts/truetype/NotoSerifCJK-*.ttc

%changelog
%autochangelog
