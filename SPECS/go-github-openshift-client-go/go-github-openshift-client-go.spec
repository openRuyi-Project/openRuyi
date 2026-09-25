# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           client-go
%define go_import_path  github.com/openshift/client-go
%define commit_id       91d71ef2122c7b41d81ea07f7f5bff89daec755c

Name:           go-github-openshift-client-go
Version:        0+git20260922.91d71ef
Release:        %autorelease
Summary:        Go clients for OpenShift APIs
License:        Apache-2.0
URL:            https://github.com/openshift/client-go
#!RemoteAsset:  sha256:dc24323dd8ecad68eed69235e6ba4ad488f481238a7cba5721615b06d458c843
Source0:        https://github.com/openshift/client-go/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/openshift/api)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/client-go)

Provides:       go(github.com/openshift/client-go) = %{version}

Requires:       go(github.com/openshift/api)
Requires:       go(github.com/spf13/pflag)
Requires:       go(k8s.io/api)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/client-go)

%description
This library provides typed clients, informers and listers for OpenShift APIs.

%prep -a
rm -rf vendor
# Upstream accidentally includes a prebuilt example executable in this snapshot.
rm -f examples/build/app

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
