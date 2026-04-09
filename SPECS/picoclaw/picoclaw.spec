# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           picoclaw
%define go_import_path  github.com/sipeed/picoclaw

Name:           picoclaw
Version:        0.2.3
Release:        %autorelease
Summary:        Tiny, Fast, and Deployable anywhere — automate the mundane, unleash your creativity
License:        MIT
URL:            https://github.com/sipeed/picoclaw
#!RemoteAsset
Source0:        https://github.com/sipeed/picoclaw/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
# TODO: Use vendor mode for now. use build dependencies later  - Julian
#!RemoteAsset
Source1:        https://github.com/software-vendor/go-picoclaw-vendor/releases/download/v%{version}/picoclaw-v%{version}-vendor.tar.gz

BuildRequires:  go
BuildRequires:  go-rpm-macros

%description
PicoClaw is an ultra-lightweight personal AI Assistant
inspired by NanoBot, refactored from the ground up in Go
through a self-bootstrapping process, where the AI agent
itself drove the entire architectural migration and code optimization.

%prep
%autosetup
%setup -q -D -T -a 1 -n %{name}-%{version}

%build
export GO111MODULE=on
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
export GOFLAGS="-buildmode=pie -mod=vendor -trimpath -modcacherw"
go generate ./...
go build -v -o %{_name} ./cmd/picoclaw
go build -v -o %{_name}-launcher ./web/backend
go build -v -o %{_name}-launcher-tui ./cmd/picoclaw-launcher-tui

%install
install -D -m 0755 %{_name} %{buildroot}%{_bindir}/%{_name}
install -D -m 0755 %{_name}-launcher %{buildroot}%{_bindir}/%{_name}-launcher
install -D -m 0755 %{_name}-launcher-tui %{buildroot}%{_bindir}/%{_name}-launcher-tui

%check
export GO111MODULE=on
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
# TODO: go_test_ignore_failure manually without buildsystem - Julian
go test -v ./... || :

%files
%license LICENSE*
%doc README*
%{_bindir}/%{_name}
%{_bindir}/%{_name}-launcher
%{_bindir}/%{_name}-launcher-tui

%changelog
%autochangelog
