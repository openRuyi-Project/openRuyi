# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cryptography

Name:           python-%{srcname}
Version:        46.0.3
Release:        %autorelease
Summary:        PyCA's cryptography library
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://cryptography.io/en/latest/
VCS:            git:https://github.com/pyca/cryptography
#!RemoteAsset:  sha256:a8b17438104fed022ce745b362294d9ce35b4c2e45c1d958ad4a4b019285f4a1
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
# TODO: Remove the vendor source after
#!RemoteAsset:  sha256:07bef086335518cee7a8dee01ded2718ce09911b639fbb257ea0fac1820291a7
Source1:        https://github.com/TakoPack/%{name}-vendor/releases/download/vendor-%{version}/%{srcname}-%{version}-vendor.tar.bz2
BuildSystem:    pyproject

BuildOption(prep):  -a1
BuildOption(install):  %{srcname}

BuildRequires:  rust
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cffi)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(maturin)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       openssl

%description
cryptography is a package designed to expose cryptographic primitives and
recipes to Python developers.

%prep -a
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%generate_buildrequires
%pyproject_buildrequires

%install -p
# https://github.com/pyca/cryptography/issues/1463
find . -name .keep -print -delete

%files -f %{pyproject_files}
%doc README.rst docs
%license LICENSE LICENSE.APACHE LICENSE.BSD

%changelog
%autochangelog
