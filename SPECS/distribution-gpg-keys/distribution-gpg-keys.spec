# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Bo YU <yubo@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           distribution-gpg-keys
Version:        1.115
Release:        %autorelease
Summary:        GPG keys of various Linux distributions
License:        CC0-1.0
URL:            https://github.com/rpm-software-management/distribution-gpg-keys
#!RemoteAsset
Source:         https://github.com/rpm-software-management/distribution-gpg-keys/archive/refs/tags/%{name}-%{version}-1.tar.gz
BuildArch:      noarch

%description
GPG keys used by various Linux distributions to sign packages.

%prep
%setup -q -n distribution-gpg-keys-distribution-gpg-keys-%{version}-1

%build
#nothing to do here

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/
cp -a keys/* %{buildroot}%{_datadir}/%{name}/
# We don't want to package COPR GPG keys
rm -rf %{buildroot}%{_datadir}/%{name}/copr

%files
%license LICENSE
%doc README.md SOURCES.md
%{_datadir}/%{name}

%changelog
%autochangelog
