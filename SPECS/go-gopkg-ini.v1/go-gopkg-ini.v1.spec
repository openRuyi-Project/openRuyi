# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ini
%define go_import_path  gopkg.in/ini.v1

Name:           go-gopkg-ini.v1
Version:        1.67.2
Release:        %autorelease
Summary:        Package ini provides INI file read and write functionality in Go
License:        Apache-2.0
URL:            https://github.com/go-ini/ini
#!RemoteAsset:  sha256:0cf3ebc458c4fe0bf495759c9e3aafe668d3b9febbd91db7d52c852ad4d3875e
Source0:        https://github.com/go-ini/ini/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n ini-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(gopkg.in/ini.v1) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/stretchr/testify)
Requires:       go(gopkg.in/yaml.v3)


%description
INI

[Image: GitHub Workflow Status] (https://img.shields.io/github/checks-
status/go-ini/ini/main?logo=github&style=for-the-badge)
(https://github.com/go-ini/ini/actions?query=branch%3Amain) [Image:
GoDoc] (https://img.shields.io/badge/GoDoc-Reference-blue?style=for-the-
badge&logo=go) (https://pkg.go.dev/github.com/go-ini/ini?tab=doc)

(https://avatars0.githubusercontent.com/u/10216035?v=3&s=200)

Package ini provides INI file read and write functionality in Go.

Features

 * Load from multiple data sources(file, []byte, io.Reader and io.
   ReadCloser) with overwrites.
 * Read with recursion values.
 * Read with parent-child sections.
 * Read with auto-increment key names.
 * Read with multiple-line values.
 * Read with tons of helper methods.
 * Read and convert values to Go types.
 * Read and **WRITE** comments of sections and keys.
 * Manipulate sections, keys and comments with ease.
 * Keep sections and keys in order as you parse and save.

Installation

The minimum requirement of Go is **1.13**.

  $ go get gopkg.in/ini.v1@latest

 | [!NOTE] If you previously used github.com/go-ini/ini as the import
path
 | in your project, without updating all of your code, you can use the
 | following command to replace the import path in your go.mod:
 |
 |   go mod edit -replace github.com/go-ini/ini=gopkg.in/ini.v1@latest

Getting Help

 * Getting Started (https://ini.unknwon.io/docs/intro/getting_started)
 * API Documentation (https://gowalker.org/gopkg.in/ini.v1)
 * 中国大陆镜像：https://ini.unknwon.cn

License

This project is under Apache v2 License. See the LICENSE (/LICENSE) file
for the full license text.


%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
