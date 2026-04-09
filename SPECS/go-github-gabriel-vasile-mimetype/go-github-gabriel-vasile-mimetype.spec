# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mimetype
%define go_import_path  github.com/gabriel-vasile/mimetype

Name:           go-github-gabriel-vasile-mimetype
Version:        1.4.12
Release:        %autorelease
Summary:        A fast Golang library for media type and file extension detection, based on magic numbers
License:        MIT
URL:            https://github.com/gabriel-vasile/mimetype
#!RemoteAsset
Source0:        https://github.com/gabriel-vasile/mimetype/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/gabriel-vasile/mimetype) = %{version}

%description
mimetypeA package for detecting MIME types and extensions based on magic
numbers

Features

 * fast and precise MIME type and file extension detection
 * long list of supported MIME types (/supported_mimes.md)
 * possibility to extend (https://pkg.go.dev/github.com/gabriel-
   vasile/mimetype#example-package-Extend) with other file formats
 * common file formats are prioritized
 * text vs. binary files differentiation (https://pkg.go.dev/github.
   com/gabriel-vasile/mimetype#example-package-TextVsBinary)
 * no external dependencies
 * safe for concurrent usage

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
