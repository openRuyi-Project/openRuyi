# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fpdf
%define go_import_path  codeberg.org/go-pdf/fpdf
# No network access during tests
%define go_test_exclude_glob codeberg.org/go-pdf/fpdf/contrib/httpimg*

Name:           go-codeberg-go-pdf-fpdf
Version:        0.11.1
Release:        %autorelease
Summary:        A PDF document generator with high level support for text, drawing and images
License:        MIT
URL:            https://codeberg.org/go-pdf/fpdf
#!RemoteAsset
Source0:        https://codeberg.org/go-pdf/fpdf/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -skip ExampleFpdf_RegisterImageReader

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/boombuler/barcode)
BuildRequires:  go(github.com/phpdave11/gofpdi)
BuildRequires:  go(github.com/ruudk/golang-pdf417)
BuildRequires:  go(golang.org/x/image)

Provides:       go(codeberg.org/go-pdf/fpdf) = %{version}

Requires:       go(github.com/boombuler/barcode)
Requires:       go(github.com/phpdave11/gofpdi)
Requires:       go(github.com/ruudk/golang-pdf417)
Requires:       go(golang.org/x/image)

%description
This package implements a PDF document generator with high level
support for text, drawing and images.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
