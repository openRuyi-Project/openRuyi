# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-reem-kufi
Version:        2.0
Release:        %autorelease
Summary:        Reem Kufi variable Arabic typeface
License:        OFL-1.1-RFN
URL:            https://github.com/aliftype/reem-kufi
#!RemoteAsset:  sha256:07dffcd0f35cb780df15c1c33df4ebdb7db9178a828c76f31384f4d857d81fff
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/reem-kufi-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  fonts-rpm-macros
BuildRequires:  make
BuildRequires:  python3dist(aliftools[filters])
BuildRequires:  python3dist(fontmake)
BuildRequires:  python3dist(fonttools)
BuildRequires:  python3dist(glyphslib)
BuildRequires:  pkgconfig(python3)

%description
Reem Kufi is a geometric Arabic typeface with a variable weight axis.
It includes Latin glyphs for mixed-script documents.

%prep
%autosetup -n reem-kufi-%{version}

%build
%make_build -B PYTHON=%{python3} TAG=v%{version} fonts/ReemKufi.ttf

%install
%install_fonts fonts/ReemKufi.ttf reem-kufi

%files
%doc README.md
%license OFL.txt
%font_files reem-kufi ttf

%changelog
%autochangelog
