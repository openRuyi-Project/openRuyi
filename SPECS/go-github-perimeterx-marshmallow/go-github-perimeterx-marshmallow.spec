# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           marshmallow
%define go_import_path  github.com/perimeterx/marshmallow

Name:           go-github-perimeterx-marshmallow
Version:        1.1.5
Release:        %autorelease
Summary:        Marshmallow provides a flexible and performant JSON unmarshalling in Go. It specializes in dealing with unstructured struct - when some fields are known and some aren't, with zero performance overhead nor extra coding needed.
License:        MIT
URL:            https://github.com/perimeterx/marshmallow
#!RemoteAsset:  sha256:d4f804a42181649e45f344764b273d9610aa439ca66f4efc8906fd07acc3b624
Source0:        https://github.com/perimeterx/marshmallow/archive/refs/tags/v1.1.5.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.25 rejects example names that look like missing identifiers.
Patch0:         2000-fix-example-names-for-current-go.patch

BuildOption(prep):  -n marshmallow-1.1.5

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-test/deep)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/mailru/easyjson/jlexer)
BuildRequires:  go(github.com/ugorji/go/codec)

Provides:       go(github.com/perimeterx/marshmallow) = %{version}

Requires:       go(github.com/josharian/intern)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(github.com/mailru/easyjson/jlexer)


%description
Marshmallow

[Image: Marshmallow Campfire]
(https://raw.githubusercontent.
com/PerimeterX/marshmallow/assets/campfire.png)

[Image: CodeQL Status]
(https://img.shields.
io/github/actions/workflow/status/perimeterx/marshmallow/codeql.
yml?branch=main&logo=github&label=CodeQL)
(https://github.com/PerimeterX/marshmallow/actions/workflows/codeql.

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
