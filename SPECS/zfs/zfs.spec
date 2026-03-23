# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Sun Yuechi <sunyuechi@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Exclude dkms source files from shebang mangling
%global __brp_mangle_shebangs_exclude_from ^/%{_usrsrc}/.*$

%global _sbindir    /sbin
%global _libdir     /%{_lib}

%global _bashcompletiondir    /etc/bash_completion.d
%global _dracutdir  %{_prefix}/lib/dracut
%global _udevdir    %{_prefix}/lib/udev
%global _udevruledir    %{_prefix}/lib/udev/rules.d
%global _pkgconfigdir %{_prefix}/%{_lib}/pkgconfig

%define systemd_svcs zfs-import-cache.service zfs-import-scan.service zfs-mount.service zfs-mount@.service zfs-share.service zfs-zed.service zfs.target zfs-import.target zfs-volume-wait.service zfs-volumes.target

Name:           zfs
Version:        2.4.1
Release:        %autorelease
Summary:        Commands to control the kernel modules and libraries
License:        CDDL
URL:            https://github.com/openzfs/zfs
#!RemoteAsset
Source0:        https://github.com/openzfs/zfs/releases/download/zfs-%{version}/zfs-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(prep):  -n zfs-%{version}
BuildOption(conf):  --with-config=user
BuildOption(conf):  --with-udevdir=%{_udevdir}
BuildOption(conf):  --with-udevruledir=%{_udevruledir}
BuildOption(conf):  --with-dracutdir=%{_dracutdir}
BuildOption(conf):  --with-pamconfigsdir=%{_datadir}/pam-configs
BuildOption(conf):  --with-pammoduledir=%{_libdir}/security
BuildOption(conf):  --with-python=python3
BuildOption(conf):  --with-pkgconfigdir=%{_pkgconfigdir}
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-debug
BuildOption(conf):  --disable-debuginfo
BuildOption(conf):  --disable-asan
BuildOption(conf):  --disable-ubsan
BuildOption(conf):  --disable-pam
BuildOption(conf):  --enable-systemd
BuildOption(conf):  --with-systemdunitdir=%{_unitdir}
BuildOption(conf):  --with-systemdpresetdir=%{_presetdir}
BuildOption(conf):  --with-systemdmodulesloaddir=%{_modulesloaddir}
BuildOption(conf):  --with-systemdgeneratordir=%{_systemdgeneratordir}
BuildOption(conf):  --disable-sysvinit

BuildRequires:  make
BuildRequires:  python3
BuildRequires:  pkgconfig(zlib)
BuildRequires:  util-linux-devel
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  systemd

Requires:       openssl
# The zpool iostat/status -c scripts call some utilities like lsblk and iostat
Requires:       util-linux
Requires:       sysstat
Requires:       %{name}-kmod = %{version}
Provides:       %{name}-libs = %{version}-%{release}
Provides:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
This package contains the core ZFS command line utilities and libraries.

%package        dkms
Summary:        Kernel module(s) (dkms)
BuildArch:      noarch

Requires:       dkms >= 2.2.0.3
Requires:       gcc
Requires:       make
Requires:       perl
Requires:       diffutils
Requires:       linux-devel

Provides:       %{name}-kmod = %{version}

AutoReqProv:    no

%description    dkms
This package contains the dkms ZFS kernel modules.

%package        devel
Summary:        Development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files needed for building additional
applications against the ZFS libraries.

%package        test
Summary:        Test infrastructure
BuildRequires:  libaio-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       parted
Requires:       lsscsi
Requires:       mdadm
Requires:       bc
Requires:       ksh
Requires:       fio
Requires:       acl
Requires:       sudo
Requires:       sysstat
Requires:       libaio
Requires:       python3
AutoReqProv:    no

%description    test
This package contains test infrastructure and support scripts for
validating the file system.

%package        dracut
Summary:        Dracut module
Requires:       %{name} >= %{version}
Requires:       dracut
Requires:       /usr/bin/awk
Requires:       grep

%description    dracut
This package contains a dracut module used to construct an initramfs
image which is ZFS aware.

%prep -a
# Save a clean copy of the source tree for the dkms subpackage
cp -a %{_builddir}/zfs-%{version} %{_builddir}/zfs-%{version}-dkms

%build -a
# Generate dkms.conf for the dkms subpackage
%{_builddir}/zfs-%{version}-dkms/scripts/dkms.mkconf -n zfs -v %{version} -f %{_builddir}/zfs-%{version}-dkms/dkms.conf

%install -a
# Install dkms source
mkdir -p %{buildroot}/%{_usrsrc}
cp -rf %{_builddir}/zfs-%{version}-dkms %{buildroot}/%{_usrsrc}/zfs-%{version}

%post
%systemd_post %{systemd_svcs}

%preun
%systemd_preun %{systemd_svcs}

%postun
%systemd_postun %{systemd_svcs}

%pre dkms
echo "Running pre installation script: $0. Parameters: $*"

# Remove any existing ZFS DKMS modules to ensure clean installation
dkms_root=/var/lib/dkms
if [ -d ${dkms_root}/zfs ]; then
    cd ${dkms_root}/zfs
    for x in [[:digit:]]*; do
        [ -d "$x" ] || continue
        otherver="$x"
        if [ `dkms status -m zfs -v "$otherver" | grep -c zfs` -gt 0 ]; then
            echo "Removing old zfs dkms modules version $otherver from all kernels."
            dkms remove -m zfs -v "$otherver" --all ||:
        fi
    done
    cd ${dkms_root}
fi

%post dkms
echo "Running post installation script: $0. Parameters: $*"

# Add the module to dkms
echo "Adding zfs dkms modules version %{version} to dkms."
dkms add -m zfs -v %{version} --rpm_safe_upgrade ||:

# Install the module for the current kernel with force overwrite
echo "Installing zfs dkms modules version %{version} for the current kernel."
dkms install --force -m zfs -v %{version} ||:

%preun dkms
echo "Running pre uninstall script: $0. Parameters: $*"

# Skip removal on upgrade
if [ "$1" = "1" ]; then
    echo "This is an upgrade. Skipping pre uninstall action."
    exit 0
fi

# Remove on uninstall
if [ "$1" = "0" ]; then
    if [ `dkms status -m zfs -v %{version} | grep -c zfs` -gt 0 ]; then
        echo "Removing zfs dkms modules version %{version} from all kernels."
        dkms remove -m zfs -v %{version} --all --rpm_safe_upgrade
    fi
fi

exit 0

%files
# Core utilities
%{_sbindir}/*
%{_bindir}/raidz_test
%{_bindir}/zvol_wait
# Optional Python 3 scripts
%{_bindir}/zarcsummary
%{_bindir}/zarcstat
%{_bindir}/dbufstat
%{_bindir}/zilstat
# Man pages
%{_mandir}/man1/*
%{_mandir}/man4/*
%{_mandir}/man5/*
%{_mandir}/man7/*
%{_mandir}/man8/*
# Configuration files and scripts
%{_libexecdir}/zfs
%{_udevdir}/vdev_id
%{_udevdir}/zvol_id
%{_udevdir}/rules.d/*
%{_datadir}/zfs/compatibility.d

# systemd files only
%exclude %{_sysconfdir}/zfs/zfs-functions
%exclude %{_sysconfdir}/default/zfs

%{_unitdir}/*
%{_presetdir}/*
%{_modulesloaddir}/*
%{_systemdgeneratordir}/*

%config(noreplace) %{_sysconfdir}/zfs/zed.d/*
%config(noreplace) %{_sysconfdir}/zfs/zpool.d/*
%config(noreplace) %{_sysconfdir}/zfs/vdev_id.conf.*.example
%attr(440, root, root) %config(noreplace) %{_sysconfdir}/sudoers.d/*

%config(noreplace) %{_bashcompletiondir}/zfs
%config(noreplace) %{_bashcompletiondir}/zpool

# zfs libs
%{_libdir}/libzpool.so.*
%{_libdir}/libnvpair.so.*
%{_libdir}/libuutil.so.*
%{_libdir}/libzfs*.so.*

%files dkms
%{_usrsrc}/zfs-%{version}

%files devel
%{_pkgconfigdir}/libzfs.pc
%{_pkgconfigdir}/libzfsbootenv.pc
%{_pkgconfigdir}/libzfs_core.pc
%{_libdir}/*.so
%{_includedir}/*
%doc AUTHORS COPYRIGHT LICENSE NOTICE README.md

%files test
%{_datadir}/zfs/zfs-tests
%{_datadir}/zfs/test-runner
%{_datadir}/zfs/runfiles
%{_datadir}/zfs/*.sh

%files dracut
%doc contrib/dracut/README.md
%{_dracutdir}/modules.d/*

%exclude /usr/share/initramfs-tools

%changelog
%{?autochangelog}
