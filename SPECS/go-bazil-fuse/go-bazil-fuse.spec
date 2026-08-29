# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fuse
%define go_import_path  bazil.org/fuse
%define commit_id       62a210ff1fd54902d27be7ac05d1b13b6f323ccd

Name:           go-bazil-fuse
Version:        0+git20260720.62a210f
Release:        %autorelease
Summary:        Go library for writing FUSE userspace filesystems
License:        BSD-3-Clause
URL:            https://github.com/bazil/fuse
#!RemoteAsset:  sha256:b39f7cd4fc6ff806daeb3790743ab39864f321078e307b0e888a77ae259c500f
Source0:        https://github.com/bazil/fuse/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/tv42/httpunix)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/sys)

%description
bazil.org/fuse is a Go library for writing FUSE userspace filesystems.

%prep -a
# The Linux test assumes amd64 Stat_t field widths. Explicit conversions keep
# the test portable to architectures where those fields use narrower types.
sed -i \
    -e 's/st\.Nlink/uint64(st.Nlink)/' \
    -e 's/st\.Blksize/int64(st.Blksize)/' \
    fs/serve_linux_test.go

%check
%go_common
%__mkdir -p %{_builddir}/go/src/%{go_import_path}
%__cp -a . %{_builddir}/go/src/%{go_import_path}
cd %{_builddir}/go/src/%{go_import_path}
# Compilation failures are not sandbox failures and must remain fatal.
%__go test -vet=off %{shrink:%{go_test_flags_default}} -run '^$' ./...
# FUSE mount tests need /dev/fuse and mount privileges unavailable in OBS.
%__go test -vet=off %{shrink:%{go_test_flags_default}} ./... || :

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
