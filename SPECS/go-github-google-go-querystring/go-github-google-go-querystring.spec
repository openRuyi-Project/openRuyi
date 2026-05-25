# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-querystring
%define go_import_path  github.com/google/go-querystring

Name:           go-github-google-go-querystring
Version:        1.2.0
Release:        %autorelease
Summary:        go-querystring is Go library for encoding structs into URL query strings.
License:        BSD-3-Clause
URL:            https://github.com/google/go-querystring
#!RemoteAsset:  sha256:d28780f21377085732bc2925ee1192a29f3e4c3fab82316a714a6e14fa52e42a
Source0:        https://github.com/google/go-querystring/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-querystring-1.2.0

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)

Provides:       go(github.com/google/go-querystring) = %{version}
Provides:       go(github.com/google/go-querystring/query) = %{version}

Requires:       go(github.com/google/go-cmp)


%description
go-querystring

[Image: Go Reference] (https://pkg.go.dev/badge/github.com/google/go-
querystring/query.svg) (https://pkg.go.dev/github.com/google/go-
querystring/query) [Image: Test Status] (https://github.com/google/go-
querystring/workflows/tests/badge.svg) (https://github.com/google/go-
querystring/actions?query=workflow%3Atests) [Image: Test Coverage]
(https://codecov.io/gh/google/go-
querystring/branch/master/graph/badge.svg)
(https://codecov.io/gh/google/go-querystring)

go-querystring is a Go library for encoding structs into URL query
parameters.

Usage

  import "github.com/google/go-querystring/query"

go-querystring is designed to assist in scenarios where you want to
construct a URL using a struct that represents the URL query parameters.
You might do this to enforce the type safety of your parameters, for
example, as is done in the go-github (https://github.com/google/go-
github/commit/994f6f8405f052a117d2d0b500054341048fbb08) library.

The query package exports a single Values() function.  A simple example:

  type Options struct {
    Query   string `url:"q"`
    ShowAll bool   `url:"all"`
    Page    int    `url:"page"`
  }

  opt := Options{ "foo", true, 2 }
  v, _ := query.Values(opt)
  fmt.Print(v.Encode()) // will output: "q=foo&all=true&page=2"

See the package godocs (https://pkg.go.dev/github.com/google/go-
querystring/query) for complete documentation on supported types and
formatting options.

Alternatives

If you are looking for a library that can both encode and decode query
strings, you might consider one of these alternatives:

 * (https://github.com/gorilla/schema)
 * (https://github.com/pasztorpisti/qs)
 * (https://github.com/hetiansu5/urlquery)
 * (https://github.com/ggicci/httpin) (decoder only)


%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
