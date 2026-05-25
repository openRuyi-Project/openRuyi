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
Summary:        Flexible JSON unmarshalling library for Go
License:        MIT
URL:            https://github.com/perimeterx/marshmallow
#!RemoteAsset:  sha256:d4f804a42181649e45f344764b273d9610aa439ca66f4efc8906fd07acc3b624
Source0:        https://github.com/perimeterx/marshmallow/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.25 rejects example names that look like missing identifiers. - HNO3Miracle
Patch2000:      2000-fix-example-names-for-current-go.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-test/deep)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/ugorji/go/codec)

Provides:       go(github.com/perimeterx/marshmallow) = %{version}

Requires:       go(github.com/josharian/intern)
Requires:       go(github.com/mailru/easyjson)

%description
Marshmallow provides flexible and performant JSON unmarshalling helpers for Go.

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
