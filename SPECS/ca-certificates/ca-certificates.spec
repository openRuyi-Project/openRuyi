# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ca-certificates
# Date based, manually update from URL. Also no VCS.
Version:        20251015
Release:        %autorelease
Summary:        Utilities for system wide CA certificate installation
License:        GPL-2.0-or-later
URL:            https://src.fedoraproject.org/rpms/ca-certificates
Source0:        update-ca-trust
# TODO: convert this to man page once we have asciidoc
Source1:        update-ca-trust.8.txt
Source2:        README.etc
Source3:        README.etcssl
Source4:        README.extr
Source5:        README.java
Source6:        README.src
Source7:        README.usr
BuildRequires:  p11-kit-devel
BuildRequires:  coreutils
BuildRequires:  bash
BuildRequires:  findutils

Requires:       p11-kit
Requires(post): p11-kit
Requires(post): bash
Requires(post): findutils
Requires(post): grep
Requires(post): sed

Requires:       ca-certificates-mozilla

%description
Update-ca-certificates is intended to keep the certificate stores of
SSL libraries like OpenSSL or GnuTLS in sync with the system's CA
certificate store that is managed by p11-kit.

%prep

%build

%install
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/pki/tls/certs
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/ssl
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/pki/ca-trust/source
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/pki/ca-trust/source/anchors
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/pki/ca-trust/source/blocklist
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted/pem
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted/pem/directory-hash
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted/java
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted/edk2
mkdir -p -m 755 %{buildroot}%{_datadir}/pki/ca-trust-source
mkdir -p -m 755 %{buildroot}%{_datadir}/pki/ca-trust-source/anchors
mkdir -p -m 755 %{buildroot}%{_datadir}/pki/ca-trust-source/blocklist
mkdir -p -m 755 %{buildroot}%{_datadir}/pki/ca-trust-legacy
mkdir -p -m 755 %{buildroot}%{_bindir}

install -p -m 755 %{SOURCE0} %{buildroot}%{_bindir}/update-ca-trust
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/ca-trust/README
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/ssl/README
install -p -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted/README
install -p -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted/java/README
install -p -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/pki/ca-trust/source/README
install -p -m 644 %{SOURCE7} %{buildroot}%{_datadir}/pki/ca-trust-source/README


# touch ghosted files that will be extracted dynamically
# Set chmod 444 to use identical permission
touch %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
chmod 444 %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
touch %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted/pem/email-ca-bundle.pem
chmod 444 %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted/pem/email-ca-bundle.pem
touch %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted/pem/objsign-ca-bundle.pem
chmod 444 %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted/pem/objsign-ca-bundle.pem
touch %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted/edk2/cacerts.bin
chmod 444 %{buildroot}%{_sysconfdir}/pki/ca-trust/extracted/edk2/cacerts.bin

# Compatibility symlink
ln -s %{_sysconfdir}/pki/tls/certs %{buildroot}%{_sysconfdir}/ssl/certs
ln -s %{_sysconfdir}/pki/tls/openssl.cnf %{buildroot}%{_sysconfdir}/ssl/openssl.cnf
ln -s %{_sysconfdir}/pki/tls/ct_log_list.cnf %{buildroot}%{_sysconfdir}/ssl/ct_log_list.cnf

%pre
if [ $1 -gt 1 ] ; then
    # Remove the old symlinks
    rm -f %{pkidir}/tls/cert.pem
    rm -f %{pkidir}/tls/certs/ca-bundle.crt
    rm -f %{pkidir}/tls/certs/ca-bundle.trust.crt
    rm -f %{pkidir}/tls/certs/ca-certificates.crt
    rm -f %{_sysconfdir}/ssl/cert.pem
fi

%post
# if ln is available, go ahead and run the ca-legacy and update
# scripts. If not, wait until %posttrans.
if [ -x %{_bindir}/ln ]; then
    %{_bindir}/update-ca-trust || true
fi

%posttrans
# When coreutils is installing with ca-certificates
# we need to wait until coreutils install to
# run our update since update requires ln to complete.
# There is a circular dependency here where
# ca-certificates depends on coreutils
# coreutils depends on openssl
# openssl depends on ca-certificates
# so we run the scripts here too, in case we couldn't run them in
# post. If we *could* run them in post this is an unnecessary
# duplication, but it shouldn't hurt anything
%{_bindir}/update-ca-trust || true

%files
%dir %{_sysconfdir}/ssl
%dir %{_sysconfdir}/pki/tls
%dir %{_sysconfdir}/pki/tls/certs
%dir %{_sysconfdir}/pki/ca-trust
%dir %{_sysconfdir}/pki/ca-trust/source
%dir %{_sysconfdir}/pki/ca-trust/source/anchors
%dir %{_sysconfdir}/pki/ca-trust/source/blocklist
%dir %{_sysconfdir}/pki/ca-trust/extracted
%dir %{_sysconfdir}/pki/ca-trust/extracted/pem
%dir %{_sysconfdir}/pki/ca-trust/extracted/java
%dir %{_sysconfdir}/pki/ca-trust/extracted/edk2
%dir %{_datadir}/pki
%dir %{_datadir}/pki/ca-trust-source
%dir %{_datadir}/pki/ca-trust-source/anchors
%dir %{_datadir}/pki/ca-trust-source/blocklist
%dir %{_datadir}/pki/ca-trust-legacy
%dir %{_sysconfdir}/pki/ca-trust/extracted/pem/directory-hash
%{_sysconfdir}/ssl/certs
%{_sysconfdir}/ssl/README
%{_sysconfdir}/ssl/openssl.cnf
%{_sysconfdir}/ssl/ct_log_list.cnf
%{_bindir}/update-ca-trust
%{_datadir}/pki/ca-trust-source/README
%{_sysconfdir}/pki/ca-trust/README
%{_sysconfdir}/pki/ca-trust/extracted/README
%{_sysconfdir}/pki/ca-trust/extracted/java/README
%{_sysconfdir}/pki/ca-trust/source/README
# files extracted files
%ghost %{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
%ghost %{_sysconfdir}/pki/ca-trust/extracted/pem/email-ca-bundle.pem
%ghost %{_sysconfdir}/pki/ca-trust/extracted/pem/objsign-ca-bundle.pem
%ghost %{_sysconfdir}/pki/ca-trust/extracted/edk2/cacerts.bin

%changelog
%autochangelog
