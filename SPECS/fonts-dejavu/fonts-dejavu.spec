# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define majver 2
%define minver 37

Name:           fonts-dejavu
Version:        %{majver}.%{minver}
Release:        %autorelease
Summary:        The DejaVu font families
License:        Bitstream-Vera AND LicenseRef-openRuyi-Public-Domain
URL:            https://dejavu-fonts.github.io/
VCS:            git:https://github.com/dejavu-fonts/dejavu-fonts
#!RemoteAsset
Source0:        https://github.com/dejavu-fonts/dejavu-fonts/archive/refs/tags/version_%{majver}_%{minver}.zip

BuildRequires:  unzip
BuildRequires:  fontforge
BuildRequires:  make
BuildRequires:  perl(Font::TTF)
BuildRequires:  perl(IO::String)
BuildRequires:  unicode-ucd

%description
The DejaVu font set is based on the “Bitstream Vera” fonts, release 1.10. Its
purpose is to provide a wider range of characters, while maintaining the
original style, using an open collaborative development process.

%prep
%autosetup -n dejavu-fonts-version_%{majver}_%{minver}

%build
%make_build VERSION=%{version} FC-LANG="" \
     BLOCKS=%{_datadir}/unicode/ucd/Blocks.txt \
     UNICODEDATA=%{_datadir}/unicode/ucd/UnicodeData.txt \
     full-ttf

%install
mkdir -p %{buildroot}%{_datadir}/fonts/truetype/
install -D -m 644 %{_builddir}/dejavu-fonts-version_%{majver}_%{minver}/build/*.ttf %{buildroot}%{_datadir}/fonts/truetype/
mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail/
install -D -m 644 %{_builddir}/dejavu-fonts-version_%{majver}_%{minver}/fontconfig/*.conf %{buildroot}%{_datadir}/fontconfig/conf.avail/

%files
%license README.md
%doc AUTHORS NEWS
%dir %{_datadir}/fonts/truetype
%{_datadir}/fonts/truetype/*.ttf
%dir %{_datadir}/fontconfig/conf.avail
%{_datadir}/fontconfig/conf.avail/*.conf

%changelog
%autochangelog
