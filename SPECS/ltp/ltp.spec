# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define ltp_prefix /opt/ltp

Name:           ltp
Version:        20260130
Release:        %autorelease
Summary:        The Linux Test Project
License:        GPL-2.0-or-later
URL:            http://linux-test-project.github.io
VCS:            git:https://github.com/linux-test-project/ltp
#!RemoteAsset
Source0:        https://github.com/linux-test-project/ltp/releases/download/%{version}/%{name}-full-%{version}.tar.xz
BuildSystem:    autotools

# Enable fsstress test in runtest/fs
Patch0001:      add-fsstress.patch
# fix output dir for cpuctl_* tests
Patch0002:      fix-cpuctl-tests-output-dir.patch

BuildOption(conf):  --prefix=%{ltp_prefix}
BuildOption(conf):  --bindir=%{ltp_prefix}/bin
BuildOption(conf):  --exec-prefix=%{ltp_prefix}/usr
BuildOption(conf):  --with-open-posix-testsuite
BuildOption(build):  LD=ld.bfd

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  linux-headers
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libaio)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  pkgconfig
BuildRequires:  xfsprogs-devel
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  xz
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(libsctp)

Recommends:     acl
Recommends:     apparmor-parser
Recommends:     apparmor-utils
Recommends:     attr
Recommends:     audit
Recommends:     bc
Recommends:     bind
Recommends:     binutils
Recommends:     dhcp-client
Recommends:     dhcp-server
Recommends:     dnsmasq
Recommends:     dosfstools
Recommends:     diffutils
Recommends:     e2fsprogs
Recommends:     ethtool
Recommends:     ima-evm-utils
Recommends:     exfat-utils
Recommends:     fuse-exfat
Recommends:     gcc
Recommends:     gdb
Recommends:     ibmtss
Recommends:     iptables
Recommends:     iputils
Recommends:     ltrace
Recommends:     lvm2
Recommends:     make
Recommends:     net-tools
Recommends:     nfs-client
Recommends:     nfs-kernel-server
Recommends:     ntfsprogs
Recommends:     numactl
Recommends:     psmisc
Recommends:     quota
Recommends:     rpcbind
Recommends:     rsync
Recommends:     squashfs
Recommends:     sssd
Recommends:     strace
Recommends:     sudo
Recommends:     sysstat
Recommends:     tcpdump
Recommends:     telnet
Recommends:     telnet-server
Recommends:     tpm-tools
Recommends:     traceroute
Recommends:     vsftpd
Recommends:     wget
Recommends:     wireguard-tools
Recommends:     xfsprogs
Recommends:     xinetd
Recommends:     expect
Recommends:     exfatprogs
Recommends:     irqbalance
Recommends:     findutils
Recommends:     iproute2
Recommends:     gzip
Recommends:     tar
Recommends:     cpio
Recommends:     procps-ng

%description
A collection of test suites to validate the reliability, robustness and
stability of Linux. It provides tools for testing the kernel and
related features.

%conf -p
make %{?_smp_mflags} autotools

%build -p
%define _lto_cflags %{nil}

%install -a
# Deal with openposix test binaries and create runtest file
mkdir -p %{buildroot}%{ltp_prefix}/testcases/bin/openposix

pushd testcases/open_posix_testsuite
# Exclude tests which are "build only"
for i in `find conformance/interfaces/ -name '*.run-test' -a ! -name '*-buildonly*'` ; do
  # create runtest openposix file
  echo `basename "$i" .run-test | sed s/-/_/` '${LTPROOT}/testcases/bin/openposix/'$i >> ../../runtest/openposix;
  # install binaries
  mkdir -p %{buildroot}%{ltp_prefix}/testcases/bin/openposix/`dirname $i`;
  cp $i %{buildroot}%{ltp_prefix}/testcases/bin/openposix/`dirname $i`;
done
popd
cp runtest/openposix %{buildroot}%{ltp_prefix}/runtest/

# Exclude tst_brkm
HARDLINKS1="tst_exit tst_fs_has_free tst_brk"
HARDLINKS2="tst_res tst_ncpus tst_ncpus_conf tst_ncpus_max tst_resm"
cd %{buildroot}%{ltp_prefix}/testcases/bin
for n in $HARDLINKS1 $HARDLINKS2; do
  ln -s -f tst_brkm $n
done

find %{buildroot} -type f -perm 775 -exec chmod 755 \{\} \;

# No tests.
%check

%files
%license COPYING
%doc README.rst INSTALL
%{ltp_prefix}

%changelog
%autochangelog
