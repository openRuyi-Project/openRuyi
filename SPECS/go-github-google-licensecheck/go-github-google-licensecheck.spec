# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           licensecheck
%define go_import_path  github.com/google/licensecheck

Name:           go-github-google-licensecheck
Version:        0.3.1
Release:        %autorelease
Summary:        The licensecheck package classifies license files and heuristically determines how well they correspond to known open source licenses.
License:        BSD-3-Clause
URL:            https://github.com/google/licensecheck
#!RemoteAsset:  sha256:9f2bd0b68cee1f4bfb0cf3143575a2a78bd045a1493354e41d52da8c5a79cfb0
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/google/licensecheck) = %{version}

%description
The licensecheck package scans source texts for known licenses.
The design aims never to give a false positive. It also reports
matches of known license URLs.

%package        tests
Summary:        Regression tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       go

%description    tests
Go regression test sources for go-github-google-licensecheck.

%files
%exclude /usr/share/gocode/src/github.com/google/licensecheck/internal/match/dict_test.go
%exclude /usr/share/gocode/src/github.com/google/licensecheck/internal/match/regexp_test.go
%exclude /usr/share/gocode/src/github.com/google/licensecheck/internal/match/rematch_test.go
%exclude /usr/share/gocode/src/github.com/google/licensecheck/internal/match/resyntax_test.go
%exclude /usr/share/gocode/src/github.com/google/licensecheck/license_test.go
%exclude /usr/share/gocode/src/github.com/google/licensecheck/old/coverage_test.go
%exclude /usr/share/gocode/src/github.com/google/licensecheck/old/license_test.go
%exclude /usr/share/gocode/src/github.com/google/licensecheck/old/normalize_test.go
%exclude /usr/share/gocode/src/github.com/google/licensecheck/old/url_test.go
%exclude /usr/share/gocode/src/github.com/google/licensecheck/type_test.go
%exclude /usr/share/gocode/src/github.com/google/licensecheck/url_test.go
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%files tests
/usr/share/gocode/src/github.com/google/licensecheck/internal/match/dict_test.go
/usr/share/gocode/src/github.com/google/licensecheck/internal/match/regexp_test.go
/usr/share/gocode/src/github.com/google/licensecheck/internal/match/rematch_test.go
/usr/share/gocode/src/github.com/google/licensecheck/internal/match/resyntax_test.go
/usr/share/gocode/src/github.com/google/licensecheck/license_test.go
/usr/share/gocode/src/github.com/google/licensecheck/old/coverage_test.go
/usr/share/gocode/src/github.com/google/licensecheck/old/license_test.go
/usr/share/gocode/src/github.com/google/licensecheck/old/normalize_test.go
/usr/share/gocode/src/github.com/google/licensecheck/old/url_test.go
/usr/share/gocode/src/github.com/google/licensecheck/type_test.go
/usr/share/gocode/src/github.com/google/licensecheck/url_test.go

%changelog
%autochangelog
