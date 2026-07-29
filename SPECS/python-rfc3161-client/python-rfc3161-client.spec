# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rfc3161-client
%global pypi_name rfc3161_client
# Upstream Cargo.toml pins the cryptography-x509 Git dependency to this tag.
%global cryptography_version 47.0.0

Name:           python-%{srcname}
Version:        1.0.7
Release:        %autorelease
Summary:        Python client for RFC 3161 timestamping services
License:        Apache-2.0 AND (Apache-2.0 OR BSD-3-Clause)
URL:            https://github.com/trailofbits/rfc3161-client
VCS:            git:https://github.com/trailofbits/rfc3161-client.git
#!RemoteAsset:  sha256:8c02330b8b09cbf88f2f5f1ecdb6e6b76c0c9bd7c4199a5068ab43b95d7ab8e5
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{pypi_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:9f8e55fe4e63613a5e1cc5819030f27b97742d720203a087802ce4ce9ceb52bb
Source1:        https://files.pythonhosted.org/packages/source/c/cryptography/cryptography-%{cryptography_version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}
BuildOption(check):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cryptography) >= 43
BuildRequires:  python3dist(maturin) >= 1.7
BuildRequires:  python3dist(maturin) < 2
BuildRequires:  python3dist(pip)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(asn1-0.24/default) >= 0.24.1
BuildRequires:  crate(hex-0.4/default) >= 0.4.0
BuildRequires:  crate(openssl-0.10/default) >= 0.10.80
BuildRequires:  crate(pyo3-0.29/abi3) >= 0.29.0
BuildRequires:  crate(pyo3-0.29/default) >= 0.29.0
BuildRequires:  crate(pyo3-0.29/extension-module) >= 0.29.0
BuildRequires:  crate(pyo3-build-config-0.29/default) >= 0.29.0
BuildRequires:  crate(pyo3-build-config-0.29/resolve-config) >= 0.29.0
BuildRequires:  crate(rand-0.10/default) >= 0.10.0
BuildRequires:  crate(self-cell-1/default) >= 1.0.0
BuildRequires:  crate(sha2-0.11/default) >= 0.11.0

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
rfc3161-client provides a Python API for requesting and verifying RFC 3161
cryptographic timestamps.

%prep -a
%rust_setup_registry
tar -xf %{SOURCE1}
rm -f Cargo.lock cryptography-%{cryptography_version}/Cargo.lock
# Build the pinned cryptography-x509 crate from an auditable source archive.
sed -i 's|cryptography-x509 = { git = "https://github.com/pyca/cryptography.git", tag = "47.0.0" }|cryptography-x509 = { path = "cryptography-%{cryptography_version}/src/rust/cryptography-x509" }|' Cargo.toml
# Keep the extracted crate attached to its own workspace metadata.
sed -i '/^resolver = "2"$/a exclude = ["cryptography-%{cryptography_version}"]' Cargo.toml
# Link to the distribution OpenSSL instead of compiling a vendored copy.
sed -i 's/openssl = { version = "0.10.80", features = \["vendored"\] }/openssl = "0.10.80"/' rust/Cargo.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE
%license cryptography-%{cryptography_version}/LICENSE
%license cryptography-%{cryptography_version}/LICENSE.APACHE
%license cryptography-%{cryptography_version}/LICENSE.BSD

%changelog
%autochangelog
