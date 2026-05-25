# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           image
%define go_import_path  golang.org/x/image

Name:           go-golang-x-image
Version:        0.34.0
Release:        %autorelease
Summary:        Go supplementary image libraries
License:        BSD-3-Clause
URL:            https://golang.org/x/image
VCS:            git:https://github.com/golang/image
#!RemoteAsset:  sha256:0fbd1db0308d71fb2fb642bf6dcee8ecde32a6f41df55c395fb2cf1613ee4609
Source0:        https://github.com/golang/image/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/text)

Provides:       go(golang.org/x/image) = %{version}
Provides:       go(golang.org/x/image/bmp) = %{version}
Provides:       go(golang.org/x/image/draw) = %{version}
Provides:       go(golang.org/x/image/font) = %{version}
Provides:       go(golang.org/x/image/font/basicfont) = %{version}
Provides:       go(golang.org/x/image/font/gofont/goregular) = %{version}
Provides:       go(golang.org/x/image/font/opentype) = %{version}
Provides:       go(golang.org/x/image/font/sfnt) = %{version}
Provides:       go(golang.org/x/image/math/f64) = %{version}
Provides:       go(golang.org/x/image/math/fixed) = %{version}
Provides:       go(golang.org/x/image/tiff) = %{version}

Requires:       go(golang.org/x/text)

%description
This repository holds supplementary Go image packages.

%prep
%autosetup -n %{_name}-%{version}

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
