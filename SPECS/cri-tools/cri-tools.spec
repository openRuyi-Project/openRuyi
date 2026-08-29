# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cri-tools
Version:        1.36.0
Release:        %autorelease
Summary:        CLI and validation tools for the Kubernetes Container Runtime Interface
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            https://github.com/kubernetes-sigs/cri-tools
#!RemoteAsset:  sha256:e0433207c55e08ab9e42e2fa3b3df3769ebae7695c145b600d79878be599e08f
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        crictl.yaml
BuildSystem:    autotools

BuildOption(build):  VERSION=%{version} binaries
BuildOption(install):  BINDIR=%{_bindir} VERSION=%{version} install

BuildRequires:  go >= 1.26.2
BuildRequires:  make
BuildRequires:  pkgconfig(bash-completion)

%description
cri-tools provides crictl for inspecting and debugging CRI-compatible container
runtimes, and critest for validating CRI runtime implementations.

%conf
# Upstream has no configure script; it builds through a Go Makefile.

%build -p
export CGO_ENABLED=0
export GO111MODULE=on
export GOFLAGS="-trimpath -modcacherw"
export GOCACHE=%{_builddir}/go-build-cache

%install -a
install -Dm0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/crictl.yaml

install -dm0755 %{buildroot}%{bash_completions_dir}
%{buildroot}%{_bindir}/crictl completion bash > %{buildroot}%{bash_completions_dir}/crictl

install -dm0755 %{buildroot}%{fish_completions_dir}
%{buildroot}%{_bindir}/crictl completion fish > %{buildroot}%{fish_completions_dir}/crictl.fish

install -dm0755 %{buildroot}%{zsh_completions_dir}
%{buildroot}%{_bindir}/crictl completion zsh > %{buildroot}%{zsh_completions_dir}/_crictl

%check
# The upstream Makefile has no check target.

%files
%doc CHANGELOG.md CONTRIBUTING.md README.md RELEASE.md docs/
%license LICENSE vendor/modules.txt
%{_bindir}/crictl
%{_bindir}/critest
%config(noreplace) %{_sysconfdir}/crictl.yaml
%{bash_completions_dir}/crictl
%{fish_completions_dir}/crictl.fish
%{zsh_completions_dir}/_crictl

%changelog
%autochangelog
