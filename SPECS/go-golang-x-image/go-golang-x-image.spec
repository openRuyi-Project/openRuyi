# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           image
%define go_import_path  golang.org/x/image

Name:           go-golang-x-image
Version:        0.43.0
Release:        %autorelease
Summary:        Go supplementary image libraries
License:        BSD-3-Clause
URL:            https://golang.org/x/image
VCS:            git:https://github.com/golang/image
#!RemoteAsset:  sha256:ef01fe3167ddd606600c2c95ae6f892cb48a881b65da991516ec7a9b0b7324e4
Source0:        https://github.com/golang/image/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/text)

Provides:       go(golang.org/x/image) = %{version}

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
