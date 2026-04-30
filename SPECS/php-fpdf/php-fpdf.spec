# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global fpdf_dir %{_datadir}/php/fpdf

Name:           php-fpdf
Version:        1.8.6
Release:        %autorelease
Summary:        PHP class to generate PDF files
License:        MIT
URL:            http://www.fpdf.org
VCS:            git:https://github.com/Setasign/FPDF.git
#!RemoteAsset:  sha256:7f09cdfc9ef75d53d79bb4d56fc7baefc80a9d87b38284f058fefe845dfe5414
Source:         https://github.com/Setasign/FPDF/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
# upstream ships a plain PHP library, no build system

BuildRequires:  php

Provides:       php-composer(setasign/fpdf) = %{version}
Requires:       php
Requires:       php-gd
Requires:       php-zlib

%description
FPDF is a PHP class that generates PDF files with pure PHP, without using
the PDFlib library. It provides high-level functions for page layout, text,
images, colors, links, font handling, and page compression.

%prep
%autosetup -n FPDF-%{version}

%install
install -d -m0755 %{buildroot}%{fpdf_dir}
cp -a fpdf.php composer.json font makefont %{buildroot}%{fpdf_dir}/

%check
php -l fpdf.php

%files
%license license.txt
%doc README.md FAQ.htm changelog.htm install.txt doc fpdf.css
%dir %{_datadir}/php
%dir %{fpdf_dir}
%{fpdf_dir}/composer.json
%{fpdf_dir}/fpdf.php
%{fpdf_dir}/font/
%{fpdf_dir}/makefont/

%changelog
%autochangelog
