# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-billy.v4
%define go_import_path  gopkg.in/src-d/go-billy.v4

Name:           go-gopkg-src-d-go-billy.v4
Version:        4.3.2
Release:        %autorelease
Summary:        Filesystem abstraction for Go, version 4
License:        Apache-2.0
URL:            https://github.com/src-d/go-billy
#!RemoteAsset:  sha256:21493a6bf113e01bc77c5d252fc9bfc7161d00a9ad35e00678836a9aada88d04
Source0:        https://github.com/src-d/go-billy/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/pty)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/check.v1)

Provides:       go(gopkg.in/src-d/go-billy.v4) = %{version}
Provides:       go(gopkg.in/src-d/go-billy.v4/helper/chroot) = %{version}
Provides:       go(gopkg.in/src-d/go-billy.v4/helper/mount) = %{version}
Provides:       go(gopkg.in/src-d/go-billy.v4/helper/polyfill) = %{version}
Provides:       go(gopkg.in/src-d/go-billy.v4/helper/temporal) = %{version}
Provides:       go(gopkg.in/src-d/go-billy.v4/memfs) = %{version}
Provides:       go(gopkg.in/src-d/go-billy.v4/osfs) = %{version}
Provides:       go(gopkg.in/src-d/go-billy.v4/test) = %{version}
Provides:       go(gopkg.in/src-d/go-billy.v4/util) = %{version}

Requires:       go(github.com/kr/pretty)
Requires:       go(github.com/kr/pty)
Requires:       go(golang.org/x/sys)
Requires:       go(gopkg.in/check.v1)

%description
Billy provides filesystem interfaces and implementations for operating
system and in-memory filesystems using the version 4 import path.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
