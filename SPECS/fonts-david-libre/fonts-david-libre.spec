# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 15496c1be77e35f3fa3d0df14a2c2c6f9adfd297

Name:           fonts-david-libre
Version:        1.100
Release:        %autorelease
Summary:        David Libre Hebrew serif typeface
License:        OFL-1.1-RFN
URL:            https://github.com/meirsadan/david-libre
#!RemoteAsset:  sha256:b9e59adaa132ee7d5f6b724658a6668597062488a378695d025cd75019cc20c7
Source0:        %{url}/archive/%{commit}.tar.gz#/david-libre-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  fonts-rpm-macros
BuildRequires:  python3dist(fontmake)
BuildRequires:  ttfautohint

%description
David Libre is a serif typeface based on David Hadash Formal. It includes
Hebrew letters and pointing, Latin letters, and three weights.

%prep
%autosetup -n david-libre-%{commit}

%build
fontmake -g sources/DavidLibre.glyphs -i -o ttf --autohint --output-dir built

%install
%install_fonts built/*.ttf david-libre

%files
%doc AUTHORS.txt CONTRIBUTORS.txt README.md
%license OFL.txt
%font_files david-libre ttf

%changelog
%autochangelog
