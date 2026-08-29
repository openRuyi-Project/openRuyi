# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define hyear  2026
%define hmonth 01
%define hday   01

Name:           fonts-noto
Version:        %{hyear}.%{hmonth}.%{hday}
Release:        %autorelease
Summary:        All Google Noto Fonts except CJK and Emoji
License:        OFL-1.1
URL:            https://notofonts.github.io/
VCS:            git:https://github.com/notofonts/notofonts.github.io
#!RemoteAsset:  sha256:f1bec0dd722fcfcb0aa75c803530e3a8ae4e0dd59e5b93a52dd8f57d5494ef44
Source0:        https://github.com/notofonts/notofonts.github.io/archive/refs/tags/noto-monthly-release-%{hyear}.%{hmonth}.%{hday}.tar.gz
BuildArch:      noarch

BuildRequires:  fonts-rpm-macros

# By default, we only install the variable fonts
Requires:       %{name}-vf = %{version}-%{release}

%description
Noto is a collection of high-quality fonts with multiple weights and widths in sans,
serif, mono, and other styles, in more than 1,000 languages and over 150 writing systems.

%package        vf
Summary:        Variable fonts in Noto font families

%description    vf
Noto is a collection of high-quality fonts with multiple weights and widths in sans,
serif, mono, and other styles, in more than 1,000 languages and over 150 writing systems.

This package contains variable fonts in Noto font families.

%package        static
Summary:        Static fonts in Noto font families

%description    static
Noto is a collection of high-quality fonts with multiple weights and widths in sans,
serif, mono, and other styles, in more than 1,000 languages and over 150 writing systems.

This package contains static fonts in Noto font families.

%prep
%autosetup -c
# License file needed
cp notofonts.github.io-noto-monthly-release-%{hyear}.%{hmonth}.%{hday}/fonts/LICENSE .

%build
# No build required

%install
# Install vf fonts (variable) into the noto-vf subdirectory
%install_fonts */fonts/*/unhinted/slim-variable-ttf/Noto*.ttf noto-vf

# Install static fonts into the noto-static subdirectory
%install_fonts */fonts/*/unhinted/ttf/Noto*.ttf noto-static
%install_fonts */fonts/*/hinted/ttf/Noto*.ttf noto-static

%files
%license LICENSE

%files vf
%license LICENSE
%font_files noto-vf ttf

%files static
%license LICENSE
%font_files noto-static ttf

%changelog
%autochangelog
