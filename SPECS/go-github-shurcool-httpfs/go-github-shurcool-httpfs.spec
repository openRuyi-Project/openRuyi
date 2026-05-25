# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           httpfs
%define go_import_path  github.com/shurcooL/httpfs
%define commit_id f1e31cf0ba5cd0d9306d6bae7602feadf4ad65cb

Name:           go-github-shurcool-httpfs
Version:        0+git20230704.f1e31cf
Release:        %autorelease
Summary:        Collection of Go packages for working with the http.FileSystem interface.
License:        MIT
URL:            https://github.com/shurcooL/httpfs
#!RemoteAsset:  sha256:9b5be5b56221d99817d758193290521e12a9c8d981b117751fecae9209744b74
Source0:        https://github.com/shurcooL/httpfs/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n httpfs-f1e31cf0ba5cd0d9306d6bae7602feadf4ad65cb
# The remaining packages either import golang.org/x/tools/godoc/vfs/httpfs,
# which is not provided by the current go-golang-x-tools package in openRuyi,
# or contain no tests after those packages are excluded.
%define go_test_exclude_glob %{go_import_path}*

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/shurcooL/httpgzip)
BuildRequires:  go(golang.org/x/tools/godoc/vfs/httpfs)
BuildRequires:  go(golang.org/x/tools/godoc/vfs/mapfs)

Provides:       go(github.com/shurcooL/httpfs) = %{version}
Provides:       go(github.com/shurcooL/httpfs/filter) = %{version}
Provides:       go(github.com/shurcooL/httpfs/html/vfstemplate) = %{version}
Provides:       go(github.com/shurcooL/httpfs/httputil) = %{version}
Provides:       go(github.com/shurcooL/httpfs/path/vfspath) = %{version}
Provides:       go(github.com/shurcooL/httpfs/text/vfstemplate) = %{version}
Provides:       go(github.com/shurcooL/httpfs/union) = %{version}
Provides:       go(github.com/shurcooL/httpfs/vfsutil) = %{version}

Requires:       go(github.com/shurcooL/httpgzip)


%description
httpfs

[Image: Go Reference]
(https://pkg.go.dev/badge/github.com/shurcooL/httpfs.svg)
(https://pkg.go.dev/github.com/shurcooL/httpfs)

Collection of Go packages for working with the http.FileSystem
(https://go.dev/pkg/net/http#FileSystem) interface.

Installation


%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
