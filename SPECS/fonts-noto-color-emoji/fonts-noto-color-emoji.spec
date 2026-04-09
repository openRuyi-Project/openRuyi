# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-noto-color-emoji
Version:        2.051
Release:        %autorelease
Summary:        Noto Color Emoji font
License:        OFL-1.1
URL:            https://notofonts.github.io/
VCS:            git:https://github.com/googlefonts/noto-emoji
#!RemoteAsset
Source0:        https://github.com/googlefonts/noto-emoji/raw/refs/tags/v%{version}/fonts/NotoColorEmoji.ttf
#!RemoteAsset
Source1:        https://github.com/googlefonts/noto-emoji/raw/refs/tags/v%{version}/LICENSE
BuildArch:      noarch

Requires:       %{name}-static = %{version}-%{release}

%description
Noto is a collection of high-quality fonts with multiple weights and widths in sans,
serif, mono, and other styles, in more than 1,000 languages and over 150 writing systems.

This package contains Noto Color Emoji font.

%package        static
Summary:        Static fonts in Noto Color Emoji font

%description    static
Noto is a collection of high-quality fonts with multiple weights and widths in sans,
serif, mono, and other styles, in more than 1,000 languages and over 150 writing systems.

This package contains Noto Color Emoji static fonts for static font support.

%prep
cp %{SOURCE0} %{SOURCE1} .

%build
# No build required

%install
# Install static fonts
mkdir -p %{buildroot}%{_datadir}/fonts/truetype
cp NotoColorEmoji.ttf %{buildroot}%{_datadir}/fonts/truetype

%files

%files static
%license LICENSE
%{_datadir}/fonts/truetype/NotoColorEmoji.ttf

%changelog
%autochangelog
