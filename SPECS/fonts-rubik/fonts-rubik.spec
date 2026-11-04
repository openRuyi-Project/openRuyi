# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit e337a5f69a9bea30e58d05bd40184d79cc099628

Name:           fonts-rubik
Version:        2.300
Release:        %autorelease
Summary:        Rubik variable sans-serif typeface
License:        OFL-1.1
URL:            https://github.com/googlefonts/rubik
#!RemoteAsset:  sha256:084747d015f017e784d5e9673c1f6479ab36100e3fead20573fef3623e438334
Source0:        %{url}/archive/%{commit}.tar.gz#/rubik-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  fonts-rpm-macros
BuildRequires:  python3dist(fontmake)
BuildRequires:  pkgconfig(python3)

%description
Rubik is a sans-serif family with rounded corners. Its upright and italic
fonts cover Hebrew, Cyrillic and Latin and support a variable weight axis.

%prep
%autosetup -n rubik-%{commit}
chmod 0644 AUTHORS.txt CONTRIBUTORS.txt

%build
mkdir built
fontmake -g sources/Rubik.glyphs -o variable --output-path built/Rubik.ttf
fontmake -g sources/Rubik-Italic.glyphs -o variable --output-path built/Rubik-Italic.ttf

%install
%install_fonts built/*.ttf rubik

%files
%doc AUTHORS.txt CONTRIBUTORS.txt README.md
%license OFL.txt
%font_files rubik ttf

%changelog
%autochangelog
