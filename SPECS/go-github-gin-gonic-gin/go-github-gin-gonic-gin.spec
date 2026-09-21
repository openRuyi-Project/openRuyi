# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gin
%define go_import_path  github.com/gin-gonic/gin

Name:           go-github-gin-gonic-gin
Version:        1.10.0
Release:        %autorelease
Summary:        Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.
License:        MIT
URL:            https://github.com/gin-gonic/gin
#!RemoteAsset:  sha256:28c0b8cc8bcccf4bceb1a77c3d0993a271dab7848f070b67beb7681f9c558479
Source0:        https://github.com/gin-gonic/gin/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/gin-gonic/gin/commit/b38c59de7fef67400a1c98efeae700a689c45783
Patch0:         0001-change-Unwrap-method-receiver-to-value-type.patch
# https://github.com/gin-gonic/gin/commit/cf4775283ec30cda685355b5016c5abd2a56884e
Patch1:         0002-test-yaml-rendering-semantically.patch

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gin-contrib/sse)
BuildRequires:  go(github.com/go-playground/validator/v10)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/ugorji/go/codec)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(google.golang.org/protobuf/proto)
BuildRequires:  go(gopkg.in/yaml.v3)
# For tests.
BuildRequires:  tzdata

Provides:       go(github.com/gin-gonic/gin) = %{version}

Requires:       go(github.com/gin-contrib/sse)
Requires:       go(github.com/go-playground/validator/v10)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/pelletier/go-toml/v2)
Requires:       go(github.com/ugorji/go/codec)
Requires:       go(golang.org/x/net)
Requires:       go(google.golang.org/protobuf/proto)
Requires:       go(gopkg.in/yaml.v3)

%description
Gin is a high-performance HTTP web framework written in Go
(https://go.dev/). It provides a Martini-like API but with significantly
better performance—up to 40 times faster—thanks to httprouter
(https://github.com/julienschmidt/httprouter). Gin is designed for
building REST APIs, web applications, and microservices where speed and
developer productivity are essential.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
