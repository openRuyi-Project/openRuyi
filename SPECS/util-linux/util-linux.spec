# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           util-linux
Version:        2.41.3
Release:        %autorelease
Summary:        A collection of basic system utilities
License:        GPL-2.0-or-later and others
URL:            https://www.kernel.org/pub/linux/utils/util-linux/
VCS:            git:https://git.kernel.org/pub/scm/utils/util-linux/util-linux.git
#!RemoteAsset:  sha256:3330d873f0fceb5560b89a7dc14e4f3288bbd880e96903ed9b50ec2b5799e58b
Source0:        https://www.kernel.org/pub/linux/utils/util-linux/v2.41/util-linux-%{version}.tar.xz
# These files define the default behavior for openRuyi.
Source10:       login.pam
Source11:       su-l.pam
Source12:       runuser.pam
Source13:       runuser-l.pam
Source14:       chfn.pam
Source15:       60-rfkill.rules
BuildSystem:    autotools

# --- Essential Patches ---
# Ensures /var/log/lastlog is created correctly.
Patch0:         login-lastlog-create.patch
# Integrates with systemd's motd.d directory.
Patch1:         login-default-motd-file.patch
# Fixes an issue with the EROFS filesystem.
Patch2:         0001-libmount-disable-EROFS-backing-file-support.patch

# Configure options for a modern, feature-rich build.
BuildOption(conf):  --with-systemdsystemunitdir=%{_unitdir}
BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --enable-chfn-chsh
BuildOption(conf):  --enable-login
BuildOption(conf):  --enable-su
BuildOption(conf):  --with-python=3
BuildOption(conf):  --with-systemd
BuildOption(conf):  --with-udev
BuildOption(conf):  --with-selinux
BuildOption(conf):  --without-slang
BuildOption(conf):  --disable-makeinstall-chown
BuildOption(conf):  --enable-nologin
BuildOption(conf):  --disable-logger

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  python3-libs
BuildRequires:  pkgconfig(audit)
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libxcrypt)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libcryptsetup)
BuildRequires:  pkgconfig(libeconf)
BuildRequires:  pkgconfig(systemd)

Provides:       eject
Provides:       rfkill
Provides:       hardlink

Requires:       libuuid%{?_isa} = %{version}-%{release}
Requires:       libblkid%{?_isa} = %{version}-%{release}
Requires:       libmount%{?_isa} = %{version}-%{release}
Requires:       libsmartcols%{?_isa} = %{version}-%{release}
Requires:       libfdisk%{?_isa} = %{version}-%{release}
Requires:       liblastlog2%{?_isa} = %{version}-%{release}
Requires:       audit
Requires:       ncurses
Requires:       pam
Requires:       readline
Requires:       zlib

%description
The util-linux package contains a large variety of low-level system
utilities that are necessary for a Linux system to function. It includes
tools like fdisk, mount, login, and more.

%package     -n libuuid
Summary:        Universally unique ID library

%description -n libuuid
The libuuid library generates and parses 128-bit universally unique IDs (UUIDs).

%package     -n libblkid
Summary:        Block device ID library
Requires:       libuuid%{?_isa} = %{version}-%{release}

%description -n libblkid
The libblkid library is used for block device identification.

%package     -n libmount
Summary:        Device mounting library
Requires:       libblkid%{?_isa} = %{version}-%{release}

%description -n libmount
The libmount library is used for mounting and unmounting filesystems.

%package     -n libsmartcols
Summary:        Column-based text formatting library

%description -n libsmartcols
The libsmartcols library is used for formatting text output in columns.

%package     -n libfdisk
Summary:        Partitioning library for fdisk-like programs

%description -n libfdisk
The libfdisk library provides functions for manipulating disk partition tables.

%package     -n liblastlog2
Summary:        The lastlog2 database library and PAM module

%description -n liblastlog2
This is the lastlog database library and PAM module, part of util-linux.

%package     -n uuidd
Summary:        Helper daemon to guarantee uniqueness of time-based UUIDs
Requires:       libuuid%{?_isa} = %{version}-%{release}
%{?systemd_requires}
Requires(pre): shadow

%description -n uuidd
The uuidd daemon guarantees uniqueness of time-based UUID generation.

%package     -n python-libmount
Summary:        Python bindings for libmount
Provides:       python3-libmount
%python_provide python3-libmount
Requires:       libmount%{?_isa} = %{version}-%{release}
Requires:       python3

%description -n python-libmount
This package contains the Python bindings for the libmount library,
which is used for mounting and unmounting filesystems.

%package        devel
Summary:        Development files for util-linux libraries
Requires:       libuuid%{?_isa} = %{version}-%{release}
Requires:       libblkid%{?_isa} = %{version}-%{release}
Requires:       libmount%{?_isa} = %{version}-%{release}
Requires:       libsmartcols%{?_isa} = %{version}-%{release}
Requires:       libfdisk%{?_isa} = %{version}-%{release}
Requires:       liblastlog2%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(zlib)

%description    devel
This package contains all header files, static libraries, and development
symlinks for the libraries included in util-linux.

%env -p
# Regenerate autotools files in case patches touched them.
autoreconf -fiv

%install -p
%if "%{_sbindir}" == "%{_bindir}"
mkdir -p %{buildroot}%{_sbindir}
ln -s %{buildroot}%{_sbindir} %{buildroot}/%{_prefix}/sbin
%endif


%install -a
%if "%{_sbindir}" == "%{_bindir}"
unlink %{buildroot}/%{_prefix}/sbin
%endif
install -Dm644 %{SOURCE10} %{buildroot}%{_sysconfdir}/pam.d/login
install -Dm644 %{SOURCE11} %{buildroot}%{_sysconfdir}/pam.d/su-l
install -Dm644 %{SOURCE12} %{buildroot}%{_sysconfdir}/pam.d/runuser
install -Dm644 %{SOURCE13} %{buildroot}%{_sysconfdir}/pam.d/runuser-l
install -Dm644 %{SOURCE14} %{buildroot}%{_sysconfdir}/pam.d/chfn

install -Dm644 %{SOURCE15} %{buildroot}%{_udevrulesdir}/60-rfkill.rules

%find_lang %{name} --generate-subpackages

%ifarch riscv64
# FIXME: script/options fails on riscv64
%check -p
export TS_OPT_script_options_known_fail=yes
export TS_OPT_script_options_show_diff=yes
%endif

%post -n liblastlog2
%systemd_post lastlog2-import.service
%postun -n liblastlog2
%systemd_postun lastlog2-import.service

%post -n uuidd
%systemd_post uuidd.service uuidd.socket
%preun -n uuidd
%systemd_preun uuidd.service uuidd.socket
%postun -n uuidd
%systemd_postun_with_restart uuidd.service uuidd.socket

%files
%license COPYING
%doc NEWS
%doc %{_docdir}/util-linux/*
# Core tools and their man pages

%{_bindir}/bits
%{_bindir}/cal
%{_bindir}/chmem
%{_bindir}/choom
%{_bindir}/col
%{_bindir}/colcrt
%{_bindir}/colrm
%{_bindir}/column
%{_bindir}/coresched
%{_bindir}/eject
%{_bindir}/enosys
%{_bindir}/exch
%{_bindir}/fallocate
%{_bindir}/fincore
%{_bindir}/fadvise
%{_bindir}/getopt
%{_bindir}/hexdump
%{_bindir}/irqtop
%{_bindir}/isosize
%{_bindir}/kill
%{_bindir}/last
%{_bindir}/lastb
%{_bindir}/lastlog2
%{_bindir}/look
%{_bindir}/lsblk
%{_bindir}/lscpu
%{_bindir}/lsclocks
%{_bindir}/lsfd
%{_bindir}/lsipc
%{_bindir}/lsirq
%{_bindir}/lslocks
%{_bindir}/lslogins
%{_bindir}/lsmem
%{_bindir}/lsns
%{_bindir}/mcookie
%{_bindir}/mesg
%{_bindir}/namei
%{_bindir}/pipesz
%{_bindir}/prlimit
%{_bindir}/rename
%{_bindir}/rev
%{_bindir}/setarch
%{_bindir}/setpgid
%{_bindir}/setpriv
%{_bindir}/setterm
%{_bindir}/uclampset
%{_bindir}/ul
%{_bindir}/utmpdump
%{_bindir}/uuidgen
%{_bindir}/uuidparse
%{_bindir}/waitpid
%{_bindir}/wall
%{_bindir}/wdctl
%{_bindir}/whereis
%{_bindir}/chrt
%{_bindir}/dmesg
%{_bindir}/findmnt
%{_bindir}/flock
%{_bindir}/hardlink
%{_bindir}/ionice
%{_bindir}/ipcmk
%{_bindir}/ipcrm
%{_bindir}/ipcs
%{_bindir}/linux32
%{_bindir}/linux64
%{_bindir}/login
%{_bindir}/more
%{_bindir}/mountpoint
%{_bindir}/nsenter
%{_bindir}/renice
%{_bindir}/script
%{_bindir}/scriptlive
%{_bindir}/scriptreplay
%{_bindir}/setsid
%{_bindir}/taskset
%{_bindir}/uname26
%{_bindir}/unshare
%ifarch x86_64
%{_bindir}/i386
%{_bindir}/x86_64
%endif
%attr(4755, root, root) %{_bindir}/su
%attr(4755, root, root) %{_bindir}/mount
%attr(4755, root, root) %{_bindir}/umount
%attr(4711, root, root) %{_bindir}/chfn
%attr(4711, root, root) %{_bindir}/chsh
%{_sbindir}/*
%ghost /etc/mtab
%config(noreplace) %{_sysconfdir}/pam.d/*
%{_unitdir}/fstrim.service
%{_unitdir}/fstrim.timer
%{_udevrulesdir}/60-rfkill.rules
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_datadir}/bash-completion/completions/*
%exclude %{_bindir}/uuidgen
%exclude %{_sbindir}/uuidd

%files -n libuuid
%{_libdir}/libuuid.so.*
%{_bindir}/uuidgen

%files -n libblkid
%{_libdir}/libblkid.so.*

%files -n libmount
%{_libdir}/libmount.so.*

%files -n libsmartcols
%{_libdir}/libsmartcols.so.*

%files -n libfdisk
%{_libdir}/libfdisk.so.*

%files -n liblastlog2
%{_libdir}/liblastlog2.so.*
%{_libdir}/security/pam_lastlog2.so
%{_unitdir}/lastlog2-import.service
%{_tmpfilesdir}/lastlog2-tmpfiles.conf

%files -n uuidd
%{_sbindir}/uuidd
%{_unitdir}/uuidd.service
%{_unitdir}/uuidd.socket
%{_tmpfilesdir}/uuidd-tmpfiles.conf
%{_sysusersdir}/uuidd-sysusers.conf

%files -n python-libmount
%{python3_sitearch}/libmount/

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/blkid.pc
%{_libdir}/pkgconfig/fdisk.pc
%{_libdir}/pkgconfig/lastlog2.pc
%{_libdir}/pkgconfig/mount.pc
%{_libdir}/pkgconfig/smartcols.pc
%{_libdir}/pkgconfig/uuid.pc
%{_mandir}/man3/*

%changelog
%autochangelog
