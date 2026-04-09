# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ll
%define go_import_path  github.com/olekukonko/ll

Name:           go-github-olekukonko-ll
Version:        0.1.3
Release:        %autorelease
Summary:        Simple logging for Development
License:        MIT
URL:            https://github.com/olekukonko/ll
#!RemoteAsset
Source0:        https://github.com/olekukonko/ll/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/olekukonko/cat)

Provides:       go(github.com/olekukonko/ll) = %{version}

Requires:       go(github.com/olekukonko/cat)

%description
ll is a high-performance, production-ready logging library for Go,
designed to provide **hierarchical namespaces**, **structured logging**,
**middleware pipelines**, **conditional logging**, and support for
multiple output formats, including text, JSON, colorized logs, and
compatibility with Go’s slog. It’s ideal for applications requiring fine-
grained log control, extensibility, and scalability.

Key Features

 * **Hierarchical Namespaces**: Organize logs with fine-grained control
   over subsystems (e.g., "app/db").
 * **Structured Logging**: Add key-value metadata for machine-readable
   logs.
 * **Middleware Pipeline**: Customize log processing with error-based
   rejection.
 * **Conditional Logging**: Optimize performance by skipping unnecessary
   log operations.
 * **Multiple Output Formats**: Support for text, JSON, colorized logs,
   and slog integration.
 * **Debugging Utilities**: Inspect variables (Dbg), binary data (Dump),
   and stack traces (Stack).
 * **Thread-Safe**: Built for concurrent use with mutex-protected state.
 * **Performance Optimized**: Minimal allocations and efficient
   namespace caching.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
