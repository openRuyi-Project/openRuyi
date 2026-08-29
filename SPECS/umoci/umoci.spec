# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _name umoci
%global go_import_path github.com/opencontainers/umoci

Name:           umoci
Version:        0.6.0
Release:        %autorelease
Summary:        umoci modifies Open Container images
License:        Apache-2.0
URL:            https://umo.ci/
VCS:            git:https://github.com/opencontainers/umoci
#!RemoteAsset:  sha256:8fca9947afe42c86468be9eb87e74269cb7ae2c292c2008212bd197c4c88aeec
Source0:        https://github.com/opencontainers/umoci/releases/download/v%{version}/umoci.tar.xz
BuildSystem:    golang

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go-md2man

%description
umoci is a reference implementation of the OCI image specification and
provides users with the ability to create, manipulate, and otherwise
interact with container images. It is designed to be as small and
unopinonated as possible, so as to act as a foundation for larger
systems to be built on top of.

%build
export GO111MODULE=on
export GOFLAGS="-buildmode=pie -mod=vendor -trimpath -modcacherw"
go build -v -o %{_name} .
for manpage in doc/man/*.md; do
    go-md2man -in ${manpage} > ${manpage/.md/}
done

%install
install -D -m 0755 %{_name} %{buildroot}%{_bindir}/%{_name}
install -d %{buildroot}%{_mandir}/man1
cp -p doc/man/*.1 %{buildroot}%{_mandir}/man1/

%files
%doc README.md CHANGELOG.md doc/*
%license COPYING
%{_bindir}/umoci
%{_mandir}/man1/umoci*

%changelog
%autochangelog
