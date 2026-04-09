# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           glog
%define go_import_path  github.com/golang/glog

Name:           go-github-golang-glog
Version:        1.2.5
Release:        %autorelease
Summary:        Leveled execution logs for Go
License:        Apache-2.0
URL:            https://github.com/golang/glog
#!RemoteAsset
Source0:        https://github.com/golang/glog/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)

Provides:       go(github.com/golang/glog) = %{version}

Requires:       go(github.com/google/go-cmp)

%description
This is an efficient pure Go implementation of leveled logs in the
manner of the open source C++ package *glog*
(https://github.com/google/glog).

By binding methods to booleans it is possible to use the log package
without paying the expense of evaluating the arguments to the log.
Through the -vmodule flag, the package also provides fine-grained
control
over logging at the file level.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
