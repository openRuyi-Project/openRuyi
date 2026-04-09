# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           backoff
%define go_import_path  github.com/cenkalti/backoff
# Test timeout even on amd64 - Julian
%define go_test_ignore_failure 1

Name:           go-github-cenkalti-backoff
Version:        5.0.3
Release:        %autorelease
Summary:        ⏱ The exponential backoff algorithm in Go
License:        MIT
URL:            https://github.com/cenkalti/backoff
#!RemoteAsset
Source0:        https://github.com/cenkalti/backoff/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cenkalti/backoff) = %{version}

%description
This is a Go port of the exponential backoff algorithm from Google's
HTTP Client Library for Java (https://github.com/google/google-http-java-
client/blob/da1aa993e90285ec18579f1553339b00e19b3ab5/google-http-
client/src/main/java/com/google/api/client/util/ExponentialBackOff.java).

Exponential backoff (http://en.wikipedia.org/wiki/Exponential_backoff)
is an algorithm that uses feedback to multiplicatively decrease the rate
of some process, in order to gradually find an acceptable rate. The
retries exponentially increase and stop increasing when a certain
threshold is met.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
