# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mux
%define go_import_path  github.com/minio/mux

Name:           go-github-minio-mux
Version:        1.9.2
Release:        %autorelease
Summary:        A powerful HTTP router and URL matcher for building Go web servers with 🦍
License:        BSD-3-Clause
URL:            https://github.com/minio/mux
#!RemoteAsset
Source0:        https://github.com/minio/mux/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gorilla/mux)

Provides:       go(github.com/minio/mux) = %{version}

Requires:       go(github.com/gorilla/mux)

%description
Package gorilla/mux implements a request router and dispatcher for
matching incoming requests to their respective handler.

The name mux stands for "HTTP request multiplexer". Like the standard
http.ServeMux, mux.Router matches incoming requests against a list of
registered routes and calls a handler for the route that matches the URL
or other conditions. The main features are:

 * It implements the http.Handler interface so it is compatible with the
   standard http.ServeMux.
 * Requests can be matched based on URL host, path, path prefix, schemes,
   header and query values, HTTP methods or using custom matchers.
 * URL hosts, paths and query values can have variables with an optional
   regular expression.
 * Registered URLs can be built, or "reversed", which helps maintaining
   references to resources.
 * Routes can be used as subrouters: nested routes are only tested if
   the parent route matches. This is useful to define groups of routes
   that share common conditions like a host, a path prefix or other
   repeated attributes. As a bonus, this optimizes request matching.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
