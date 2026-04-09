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
#!RemoteAsset
Source0:        https://github.com/notofonts/notofonts.github.io/archive/refs/tags/noto-monthly-release-%{hyear}.%{hmonth}.%{hday}.tar.gz
BuildArch:      noarch

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
mkdir -p %{buildroot}%{_datadir}/fonts/truetype

: > vf.file
: > static.file

# Install vf fonts
for f in */fonts/*/unhinted/slim-variable-ttf/Noto*.ttf; do
    [ -f "$f" ] || continue
    install -m 0644 -p "$f" %{buildroot}%{_datadir}/fonts/truetype/
    echo "%{_datadir}/fonts/truetype/$(basename "$f")" >> vf.file
done

# Install static fonts
for f in */fonts/*/unhinted/ttf/Noto*.ttf */fonts/*/hinted/ttf/Noto*.ttf; do
    [ -f "$f" ] || continue
    install -m 0644 -p "$f" %{buildroot}%{_datadir}/fonts/truetype/
    echo "%{_datadir}/fonts/truetype/$(basename "$f")" >> static.file
done

sort -u vf.file -o vf.file
sort -u static.file -o static.file

%files

%files vf -f vf.file
%license LICENSE

%files static -f static.file
%license LICENSE

%changelog
%autochangelog
