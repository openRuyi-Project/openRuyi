# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ca-certificates-mozilla
# Version number is NSS_BUILTINS_LIBRARY_VERSION in this file:
# http://hg.mozilla.org/projects/nss/file/default/lib/ckfw/builtins/nssckbi.h
Version:        2.84
Release:        %autorelease
Summary:        CA certificates for OpenSSL
License:        MPL-2.0
URL:            https://www.mozilla.org
# VCS: No VCS link available
# https://hg.mozilla.org/projects/nss/raw-file/default/lib/ckfw/builtins/certdata.txt
Source0:        certdata.txt
# https://hg.mozilla.org/projects/nss/raw-file/default/lib/ckfw/builtins/nssckbi.h
Source1:        nssckbi.h
# https://src.fedoraproject.org/rpms/ca-certificates/raw/rawhide/f/certdata2pem.py
Source2:        certdata2pem.py
Source3:        COPYING

BuildRequires:  ca-certificates
BuildRequires:  openssl
BuildRequires:  python3
BuildRequires:  python-rpm-macros

# for update-ca-certificates
Requires(post): ca-certificates
Requires(postun): ca-certificates

%description
This package contains some CA root certificates for OpenSSL extracted
from Mozilla Firefox

%prep
%setup -qcT

mkdir certs
cd certs
cp %{SOURCE0} .
cd ..

install -m 644 %{SOURCE3} COPYING
# Notice the version number mismatch
ver=`sed -ne '/NSS_BUILTINS_LIBRARY_VERSION /s/.*"\(.*\)"/\1/p' < "%{SOURCE1}"`
if [ "%{version}" != "$ver" ]; then
        echo "*** Version number mismatch: spec file should be version $ver"
        false
fi

%build
export LANG=en_US.UTF-8
cd certs
%{__python3} %{SOURCE2}
cd ..
(
  cat <<-EOF
	# This is a bundle of X.509 certificates of public Certificate
	# Authorities.  It was generated from the Mozilla root CA list.
	# These certificates and trust/distrust attributes use the file format accepted
	# by the p11-kit-trust module.
	#
	# Source: nss/lib/ckfw/builtins/certdata.txt
	# Source: nss/lib/ckfw/builtins/nssckbi.h
	#
	# Generated from:
	EOF
   awk '$2 == "NSS_BUILTINS_LIBRARY_VERSION" {print "# " $2 " " $3}' %{SOURCE1}
   echo '#';
   ls -1 certs/*.tmp-p11-kit | sort | xargs cat
) > %{name}.trust.p11-kit

%install
mkdir -p %{buildroot}%{_datadir}/pki/trust/
install -m 644 %{name}.trust.p11-kit "%{buildroot}%{_datadir}/pki/trust/%{name}.trust.p11-kit"

%post
update-ca-trust || true

%postun
update-ca-trust || true

%posttrans
update-ca-trust || true

%files
%license COPYING
%{_datadir}/pki/trust/

%changelog
%autochangelog
