# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           i2c-tools
Version:        4.4
Release:        %autorelease
Summary:        A heterogeneous set of I2C tools for Linux
License:        GPL-2.0-or-later
URL:            https://archive.kernel.org/oldwiki/i2c.wiki.kernel.org/index.php/I2C_Tools.html
VCS:            git:https://git.kernel.org/pub/scm/utils/i2c-tools/i2c-tools.git
#!RemoteAsset
Source0:        https://www.kernel.org/pub/software/utils/i2c-tools/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://www.kernel.org/pub/software/utils/i2c-tools/%{name}-%{version}.tar.sign
BuildSystem:    autotools

BuildOption(build):  CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
BuildOption(build):  BUILD_STATIC_LIB=0 EXTRA=eeprog
BuildOption(install):  DESTDIR=%{buildroot} PREFIX=%{_prefix} BUILD_STATIC_LIB=0
BuildOption(install):  EXTRA=eeprog libdir=%{_libdir} bindir=%{_bindir}
BuildOption(install):  sbindir=%{_sbindir}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools

Requires:       systemd-udev
Requires:       kmod
Requires:       libi2c%{?_isa} = %{version}-%{release}

%patchlist
0001-i2ctransfer-Don-t-link-with-libi2c.patch
0002-i2ctransfer-Don-t-free-memory-which-was-never-alloca.patch
0003-i2ctransfer-Prevent-msgs-overflow-with-many-paramete.patch
0004-i2ctransfer-Zero-out-memory-passed-to-ioctl.patch

%description
This package contains a heterogeneous set of I2C tools for Linux: a bus
probing tool, a chip dumper, register-level access helpers, EEPROM
decoding scripts, and more.

%package     -n python-i2c-tools
Summary:        Python bindings for Linux SMBus access through i2c-dev
License:        GPL-2.0-only
Provides:       python3-i2c-tools = %{version}-%{release}
%{?python_provide:%python_provide python3-i2c-tools}
Requires:       libi2c%{?_isa} = %{version}-%{release}

%description -n python-i2c-tools
Python bindings for Linux SMBus access through i2c-dev.

%package        perl
Summary:        i2c tools written in Perl
License:        GPL-2.0-or-later
Requires:       libi2c%{?_isa} = %{version}-%{release}

%description    perl
A collection of tools written in perl for use with i2c devices.

%package     -n libi2c
Summary:        I2C/SMBus bus access library
License:        LGPL-2.1-or-later

%description -n libi2c
libi2c offers a way for applications to interact with the devices
connected to the I2C or SMBus buses of the system.

%package     -n libi2c-devel
Summary:        Development files for the I2C library
License:        LGPL-2.1-or-later
Requires:       libi2c%{?_isa} = %{version}-%{release}

%description -n libi2c-devel
%{summary}.

# No configure script.
%conf

%build -a
pushd py-smbus
CFLAGS="$RPM_OPT_FLAGS -I../include" LDFLAGS="$RPM_LD_FLAGS" \
  %{__python3} setup.py build -b build-py3
popd


%install -a
pushd py-smbus
%{__python3} setup.py build -b build-py3 install --skip-build --root=%{buildroot}
popd

# cleanup
rm -f %{buildroot}%{_bindir}/decode-edid.pl
# Remove unpleasant DDC tools.  KMS already exposes the EDID block in sysfs,
# and edid-decode is a more complete tool than decode-edid.
rm -f %{buildroot}%{_bindir}/{ddcmon,decode-edid}

# for i2c-dev ondemand loading through kmod
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d
echo "alias char-major-89-* i2c-dev" > \
  %{buildroot}%{_sysconfdir}/modprobe.d/i2c-dev.conf
# for /dev/i2c-# creation (which are needed for kmod i2c-dev autoloading)
mkdir -p %{buildroot}%{_sysconfdir}/udev/makedev.d
for (( i = 0 ; i < 8 ; i++ )) do
  echo "i2c-$i" >> %{buildroot}%{_sysconfdir}/udev/makedev.d/99-i2c-dev.nodes
done

# auto-load i2c-dev after reboot
mkdir -p %{buildroot}%{_prefix}/lib/modules-load.d
echo 'i2c-dev' > %{buildroot}%{_prefix}/lib/modules-load.d/%{name}.conf

# no tests.
%check

#Install and uninstall scripts
%post
# load i2c-dev after the first install
if [ "$1" = 1 ] ; then
  /usr/sbin/modprobe i2c-dev
fi
exit 0

%files
%license COPYING
%doc CHANGES README eeprog/README.eeprog
%config(noreplace) %{_sysconfdir}/modprobe.d/i2c-dev.conf
%config(noreplace) %{_sysconfdir}/udev/makedev.d/99-i2c-dev.nodes
%{_prefix}/lib/modules-load.d/%{name}.conf
%{_sbindir}/i2c*
%{_sbindir}/eeprog
%exclude %{_sbindir}/i2c-stub*
%{_mandir}/man8/i2c*.8.*
%{_mandir}/man8/eeprog.8.*

%files -n python-i2c-tools
%doc py-smbus/README
%{python3_sitearch}/*

%files perl
%doc eeprom/README
%{_bindir}/decode-*
%{_sbindir}/i2c-stub*
%{_mandir}/man1/decode-*.1.*
%{_mandir}/man8/i2c-stub-from-dump.8.*

%files -n libi2c
%license COPYING.LGPL
%{_libdir}/libi2c.so.0*

%files -n libi2c-devel
%dir %{_includedir}/i2c
%{_includedir}/i2c/smbus.h
%{_libdir}/libi2c.so
%{_mandir}/man3/libi2c.3.*

%changelog
%autochangelog
