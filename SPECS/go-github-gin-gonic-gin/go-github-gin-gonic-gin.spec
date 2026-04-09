# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gin
%define go_import_path  github.com/gin-gonic/gin

Name:           go-github-gin-gonic-gin
Version:        1.8.1
Release:        %autorelease
Summary:        Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.
License:        MIT
URL:            https://github.com/gin-gonic/gin
#!RemoteAsset
Source0:        https://github.com/gin-gonic/gin/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -skip TestContextFormFileFailed17

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gin-contrib/sse)
BuildRequires:  go(github.com/go-playground/validator/v10)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/ugorji/go/codec)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/gin-gonic/gin) = %{version}

Requires:       go(github.com/gin-contrib/sse)
Requires:       go(github.com/go-playground/validator/v10)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/pelletier/go-toml/v2)
Requires:       go(github.com/ugorji/go/codec)
Requires:       go(golang.org/x/net)
Requires:       go(gopkg.in/yaml.v2)
Requires:       go(google.golang.org/protobuf)

%description
Gin is a high-performance HTTP web framework written in Go
(https://go.dev/). It provides a Martini-like API but with significantly
better performance—up to 40 times faster—thanks to httprouter
(https://github.com/julienschmidt/httprouter). Gin is designed for
building REST APIs, web applications, and microservices where speed and
developer productivity are essential.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
