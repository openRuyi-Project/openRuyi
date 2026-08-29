# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           etcd
%define go_import_path  go.etcd.io/etcd/v3
%define git_sha         d2809cf0019f84c221e026bb2ac6486d011b1d91

Name:           etcd
Version:        3.6.6
Release:        %autorelease
Summary:        Distributed reliable key-value store
License:        Apache-2.0
URL:            https://github.com/etcd-io/etcd
#!RemoteAsset:  sha256:371dd03b6ae1f6ed06496dbe53ffee5ec9126583184bf27c835047d1b0686d11
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# TODO: Use packaged Go module dependencies once the remaining etcd dependency
# closure is available in openRuyi.
#!RemoteAsset:  sha256:60d715ba2b5a22dbb8d04c9dfb7dd14689933f3759831837decd3e6461a2ec44
Source1:        https://github.com/software-vendor/go-etcd-vendor/releases/download/v%{version}/%{name}-%{version}-vendor.tar.gz
Source2:        etcd.service
Source3:        etcd.sysusers
Source4:        etcd.tmpfiles

BuildRequires:  go >= 1.24
BuildRequires:  systemd-rpm-macros

%{?systemd_requires}

%description
etcd is a strongly consistent, distributed key-value store that provides a
reliable way to store data that must be accessed by a distributed system or
cluster of machines. Kubernetes uses etcd as its primary backing store for
cluster state.

%prep
%autosetup -n %{name}-%{version}
tar -xf %{SOURCE1}

%build
export GOCACHE=%{_builddir}/go-build-cache
export GOFLAGS="-modcacherw"
export GONOSUMDB="*"
export GOPROXY=off
export GOTOOLCHAIN=local
go_ldflags="-X=go.etcd.io/etcd/api/v3/version.GitSHA=%{git_sha}"

(
    cd server
    CGO_ENABLED=0 go build -trimpath -mod=vendor -installsuffix=cgo \
        -ldflags "${go_ldflags}" -o ../bin/etcd .
)

(
    cd etcdctl
    CGO_ENABLED=0 go build -trimpath -mod=vendor -installsuffix=cgo \
        -ldflags "${go_ldflags}" -o ../bin/etcdctl .
)

(
    cd etcdutl
    CGO_ENABLED=0 go build -trimpath -mod=vendor -installsuffix=cgo \
        -ldflags "${go_ldflags}" -o ../bin/etcdutl .
)

%install
install -Dpm0755 bin/etcd %{buildroot}%{_bindir}/etcd
install -Dpm0755 bin/etcdctl %{buildroot}%{_bindir}/etcdctl
install -Dpm0755 bin/etcdutl %{buildroot}%{_bindir}/etcdutl
install -Dpm0644 %{SOURCE2} %{buildroot}%{_unitdir}/etcd.service
install -Dpm0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/etcd.conf
install -Dpm0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/etcd.conf
install -dpm0750 %{buildroot}%{_localstatedir}/lib/etcd

%check
%ifarch riscv64
export ETCD_UNSUPPORTED_ARCH=riscv64
%endif
%{buildroot}%{_bindir}/etcd --version
%{buildroot}%{_bindir}/etcdctl version
%{buildroot}%{_bindir}/etcdutl version

%pre
%sysusers_create_package %{name} %{SOURCE3}
%tmpfiles_create_package %{name} %{SOURCE4}

%post
%systemd_post etcd.service

%preun
%systemd_preun etcd.service

%postun
%systemd_postun_with_restart etcd.service

%files
%doc README.md
%license LICENSE
%{_bindir}/etcd
%{_bindir}/etcdctl
%{_bindir}/etcdutl
%{_unitdir}/etcd.service
%{_sysusersdir}/etcd.conf
%{_tmpfilesdir}/etcd.conf
%attr(0750,etcd,etcd) %dir %{_localstatedir}/lib/etcd

%changelog
%autochangelog
