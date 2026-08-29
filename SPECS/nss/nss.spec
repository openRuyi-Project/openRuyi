# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define major_version 3
%define minor_version 124
%define patch_version 0

# Check https://searchfox.org/nss/source/automation/release/nspr-version.txt
%define nspr_version 4.38.2

Name:           nss
Version:        %{major_version}.%{minor_version}.%{patch_version}
Release:        %autorelease
Summary:        Network Security Services
License:        MPL-2.0
URL:            https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS
VCS:            hg:https://hg.mozilla.org/projects/nss
#!RemoteAsset:  sha256:80da9f1cbcb267293b2248818d288bc02f874d6a34f1989a2828401d74a0bc9b
Source:         https://ftp.mozilla.org/pub/security/nss/releases/NSS_%{major_version}_%{minor_version}_RTM/src/nss-%{major_version}.%{minor_version}.tar.gz
BuildSystem:    autotools

# We don't have network in our build environment
Patch2000:      2000-skip-ocsp-policy-check-in-offline-build.patch
Patch2001:      2001-Make-dbtests-certutil-K-timeout-configurable.patch

BuildOption(build):  -C nss
BuildOption(build):  all
BuildOption(build):  BUILD_OPT=1
BuildOption(build):  NSS_USE_SYSTEM_SQLITE=1
BuildOption(build):  NSS_ENABLE_WERROR=0
BuildOption(build):  USE_64=1
BuildOption(build):  NSPR_INCLUDE_DIR=%{_includedir}/nspr
BuildOption(build):  NSPR_LIB_DIR=%{_libdir}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  perl
BuildRequires:  which
BuildRequires:  pkgconfig(nspr) >= %{nspr_version}

Requires:       nspr >= %{nspr_version}

%description
Network Security Services (NSS) is a set of libraries for developing
security-enabled client and server applications. This all-in-one package
contains the runtime libraries, development files, and command-line tools.

# No configure
%conf

%install
# no make install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_libdir}
install -d -m 755 %{buildroot}%{_includedir}/nss3
install -d -m 755 %{buildroot}%{_libdir}/pkgconfig
install -d -m 755 %{buildroot}%{_sysconfdir}/pki/nssdb

make BUILD_OPT=1 USE_64=1 -C ./nss latest
TARGET_DIR=$(cat dist/latest)
DIST_DIR=dist/$TARGET_DIR

# Use -L to follow symlinks and copy actual files instead of broken symlinks
cp -L $DIST_DIR/bin/* %{buildroot}%{_bindir}/

cp -aL dist/public/nss/*.h %{buildroot}%{_includedir}/nss3/

# Install .so and .chk files from nss/lib only (exclude nspr), following symlinks
find nss/lib -name "*.so" -path "*${TARGET_DIR}*" ! -name "libnspr*" ! -name "libplc*" ! -name "libplds*" -exec sh -c 'cp -L "$1" %{buildroot}%{_libdir}/' _ {} \;
find nss/lib -name "*.chk" -path "*${TARGET_DIR}*" -exec sh -c 'cp -L "$1" %{buildroot}%{_libdir}/' _ {} \;

cd %{buildroot}%{_libdir}
ln -snf libnss3.so libnss3.so.3
ln -snf libnssutil3.so libnssutil3.so.3
ln -snf libsmime3.so libsmime3.so.3
ln -snf libssl3.so libssl3.so.3
ln -snf libsoftokn3.so libsoftokn3.so.3

rm -f %{buildroot}%{_bindir}/{gtests,nss-gtest-all}

# need create pc
install -d -m 755 %{buildroot}%{_libdir}/pkgconfig

cat > %{buildroot}%{_libdir}/pkgconfig/nss-util.pc << EOF
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/nss3

Name: NSS-UTIL
Description: Network Security Services Utility Library
Version: %{version}
Requires: nspr >= %{nspr_version}
Libs: -L\${libdir} -lnssutil3
Cflags: -I\${includedir}
EOF

cat > %{buildroot}%{_libdir}/pkgconfig/nss.pc << EOF
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/nss3

Name: NSS
Description: Network Security Services
Version: %{version}
Requires: nspr >= %{nspr_version}, nss-util
Libs: -L\${libdir} -lssl3 -lsmime3 -lnss3
Cflags: -I\${includedir}
EOF

%check
export BUILD_OPT=1
export HOST="localhost"
export DOMSUF="localdomain"
export USE_IP=TRUE
export IP_ADDRESS="127.0.0.1"
export NSS_IGNORE_SYSTEM_POLICY=1
cd nss/tests
%ifarch riscv64
export NSS_DBTESTS_CERTUTIL_K_TIMEOUT=10
%endif
# 'tools' will take so long it's not worth it...
export NSS_TESTS="cipher lowhash cert dbtests sdr smime ssl ocsp merge ec gtests ssl_gtests policy chains"
# And we don't have network in our build environment
export NSS_SKIP_BADSSL_OCSP=1
./all.sh

%files
%license nss/COPYING
%dir %{_sysconfdir}/pki
%dir %{_sysconfdir}/pki/nssdb
%{_libdir}/lib*.so*
%{_libdir}/*.chk
%{_bindir}/*
%{_includedir}/nss3
%{_libdir}/pkgconfig/nss-util.pc
%{_libdir}/pkgconfig/nss.pc

%changelog
%autochangelog
