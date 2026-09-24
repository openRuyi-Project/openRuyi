# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           osutil
%define go_import_path  github.com/tredoe/osutil
%define go_test_include  %{go_import_path}/user/crypt/...

Name:           go-github-tredoe-osutil
Version:        1.5.0
Release:        %autorelease
Summary:        Operating system utilities for Go
License:        MPL-2.0
URL:            https://github.com/tredoe/osutil
VCS:            git:https://github.com/tredoe/osutil.git
#!RemoteAsset:  sha256:3c1f4940e85dcf2c389bb81fa9ce2709005d0fe181f3a48929e4d271bbda7d35
Source0:        https://github.com/tredoe/osutil/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n osutil-1.5.0

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/tredoe/osutil) = %{version}

%description
This package provides the github.com/tredoe/osutil Go module source.

%files
%doc README.md
%license LICENSE-MPL.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
