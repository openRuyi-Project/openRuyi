# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cni
%define go_import_path  github.com/containernetworking/cni

# Compatibility tests fetch historical CNI revisions, but OBS has no network.
%define go_test_ignore_failure 1

Name:           go-github-containernetworking-cni
Version:        1.1.2
Release:        %autorelease
Summary:        CNI library for container networking
License:        Apache-2.0
URL:            https://github.com/containernetworking/cni
#!RemoteAsset:  sha256:7d4bcaf83acdd54b3dc216f7aa5b5e1b32cb797d9c6af601a2c26b97470ed743
Source0:        https://github.com/containernetworking/cni/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/onsi/ginkgo/v2)
BuildRequires:  go(github.com/onsi/gomega)

Provides:       go(%{go_import_path}) = %{version}

%description
CNI provides APIs for invoking container network plugins and handling network
configuration and results.

%prep -a
# cnitool is a developer test helper, not an installed CNI plugin. The debug
# plugin is a separate module and is not part of the root library.
rm -rf cnitool plugins/debug

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
