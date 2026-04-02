# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test
# NOTE: When updating this package, update SELinux first.

Name:           policycoreutils
Version:        3.10
Release:        %autorelease
Summary:        SELinux policy core utilities
License:        GPL-2.0-or-later
URL:            https://github.com/SELinuxProject/selinux
#!RemoteAsset
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
#!RemoteAsset
Source2:        %{url}/releases/download/%{version}/selinux-dbus-%{version}.tar.gz
#!RemoteAsset
Source3:        %{url}/releases/download/%{version}/selinux-dbus-%{version}.tar.gz.asc
#!RemoteAsset
Source4:        %{url}/releases/download/%{version}/selinux-python-%{version}.tar.gz
#!RemoteAsset
Source5:        %{url}/releases/download/%{version}/selinux-python-%{version}.tar.gz.asc
#!RemoteAsset
Source6:        %{url}/releases/download/%{version}/selinux-gui-%{version}.tar.gz
#!RemoteAsset
Source7:        %{url}/releases/download/%{version}/selinux-gui-%{version}.tar.gz.asc
#!RemoteAsset
Source8:        %{url}/releases/download/%{version}/semodule-utils-%{version}.tar.gz
#!RemoteAsset
Source9:        %{url}/releases/download/%{version}/semodule-utils-%{version}.tar.gz.asc
BuildSystem:    autotools

# Because the way we build this pacakge, so we need
# to change the make targets
Patch0:         0001-make_targets.patch
# From https://github.com/SELinuxProject/selinux/pull/507
Patch1:         fix-discarded-qualifiers-warning-with-glib-2.43.patch

BuildOption(install):  SBINDIR="%{_sbindir}"

BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  pkg-config
BuildRequires:  libsepol-static
BuildRequires:  audit-devel
BuildRequires:  bash-completion
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libsemanage)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python-rpm-macros

Requires:       util-linux

%description
Security-enhanced Linux is a feature of the Linux┬« kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement┬«, Role-based Access
Control, and Multi-level Security.

policycoreutils contains the policy core utilities that are required
for basic operation of a SELinux system.  These utilities include
load_policy to load policies, setfiles to label filesystems, newrole
to switch roles.

%package        devel
Summary:        SELinux policy core policy devel utilities
Requires:       python-policycoreutils = %{version}-%{release}
Requires:       make
Requires:       (selinux-policy-devel if selinux-policy)

%description    devel
The policycoreutils-devel package contains the management tools use to develop policy in an SELinux environment.

%package     -n python-policycoreutils
Summary:        SELinux policy core python utilities
Provides:       python3-policycoreutils
Requires:       policycoreutils = %{version}-%{release}
Requires:       python3-libselinux
Requires:       python3-setools
Requires:       python3-libsemanage
BuildArch:      noarch

%description -n python-policycoreutils
The policycoreutils-python-utils package contains the management tools use to manage
an SELinux environment.

%package        dbus
Summary:        SELinux policy core DBUS api
Requires:       python3-policycoreutils = %{version}-%{release}
Requires:       python3-pygobject
Requires:       polkit
BuildArch:      noarch

%description    dbus
The policycoreutils-dbus package contains the management DBUS API use to manage
an SELinux environment.

%package        gui
Summary:        SELinux configuration GUI
Requires:       policycoreutils-devel = %{version}-%{release}
Requires:       python3-policycoreutils = %{version}-%{release}
Requires:       policycoreutils-dbus = %{version}-%{release}
Requires:       python3-pygobject
BuildRequires:  desktop-file-utils
BuildArch:      noarch

%description    gui
system-config-selinux is a utility for managing the SELinux environment

%package        newrole
Summary:        The newrole application for RBAC/MLS
Requires:       policycoreutils = %{version}-%{release}

%description    newrole
RBAC/MLS policy machines require newrole as a way of changing the role
or level of a logged in user.

%prep
%setup -q -a2 -a4 -a6 -a8
setools_python_pwd="$PWD/selinux-python-%{version}"
semodule_utils_pwd="$PWD/semodule-utils-%{version}"
%patch -P 0 -p1
%patch -P 1 -p2
mv ${setools_python_pwd}/audit2allow ${setools_python_pwd}/chcat ${setools_python_pwd}/semanage ${setools_python_pwd}/sepolgen ${setools_python_pwd}/sepolicy .
mv ${semodule_utils_pwd}/semodule_expand ${semodule_utils_pwd}/semodule_link ${semodule_utils_pwd}/semodule_package .

%conf
# No configure

%install -p
mkdir -p %{buildroot}%{_localstatedir}/lib/selinux
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
export PYTHON_SETUP_ARGS="$PYTHON_SETUP_ARGS --no-build-isolation"

%install -a
# dbus
(cd selinux-dbus-%{version} && make DESTDIR=%{buildroot} install)
# GUI apps
(cd selinux-gui-%{version} && make DESTDIR=%{buildroot} install)

mkdir -p %{buildroot}%{_libexecdir}/selinux/hll/
mkdir -p %{buildroot}%{_localstatedir}/lib/sepolgen

(cd selinux-python-%{version}/po && make DESTDIR=%{buildroot} install)

# Fix perms on newrole so that objcopy can process it
chmod 0755 %{buildroot}%{_bindir}/newrole

# Manually invoke the python byte compile macro for each path that needs byte
# compilation.
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/system-config-selinux

# We don't need these because we have systemd
# If we need /etc/init.d support then we can add it back
rm -f %{buildroot}%{_sbindir}/open_init_pty
rm -f %{buildroot}%{_sbindir}/run_init
rm -f %{buildroot}/usr/share/man/man8/open_init_pty.8
rm -f %{buildroot}/usr/share/man/man8/run_init.8*
rm -f %{buildroot}/etc/pam.d/run_init*

# Illegal char '@' (0x40) in: %package langpack-sr@latin
# So we can't use --generate-subpackages
%find_lang %{name}
# We changed the name of these, also can't use it here
%find_lang selinux-python
%find_lang selinux-gui

%files -f %{name}.lang
%license LICENSE
%{_sbindir}/restorecon
%{_sbindir}/restorecon_xattr
%{_sbindir}/fixfiles
%{_sbindir}/setfiles
%{_sbindir}/load_policy
%{_sbindir}/genhomedircon
%{_sbindir}/setsebool
%{_sbindir}/semodule
%{_sbindir}/unsetfiles
%if "%{_sbindir}" != "%{_bindir}"
# symlink to %%{_bindir}/sestatus
%{_sbindir}/sestatus
%endif
%{_bindir}/secon
%{_bindir}/semodule_expand
%{_bindir}/semodule_link
%{_bindir}/semodule_package
%{_bindir}/semodule_unpackage
%{_bindir}/sestatus
%{_libexecdir}/selinux/hll
%config(noreplace) %{_sysconfdir}/sestatus.conf
%{_mandir}/man5/selinux_config.5.gz
%{_mandir}/man5/sestatus.conf.5.gz
%{_mandir}/man8/fixfiles.8*
%{_mandir}/man8/load_policy.8*
%{_mandir}/man8/restorecon.8*
%{_mandir}/man8/restorecon_xattr.8*
%{_mandir}/man8/semodule.8*
%{_mandir}/man8/sestatus.8*
%{_mandir}/man8/setfiles.8*
%{_mandir}/man8/setsebool.8*
%{_mandir}/man1/secon.1*
%{_mandir}/man1/unsetfiles.1*
%{_mandir}/man8/genhomedircon.8*
%{_mandir}/man8/semodule_expand.8*
%{_mandir}/man8/semodule_link.8*
%{_mandir}/man8/semodule_unpackage.8*
%{_mandir}/man8/semodule_package.8*
%{bash_completions_dir}/setsebool

%files devel
%{_bindir}/sepolgen
%{_bindir}/sepolgen-ifgen
%{_bindir}/sepolgen-ifgen-attr-helper
%dir  /var/lib/sepolgen
/var/lib/sepolgen/perm_map
%{_bindir}/sepolicy
%{_mandir}/man8/sepolgen.8*
%{_mandir}/man8/sepolicy-booleans.8*
%{_mandir}/man8/sepolicy-generate.8*
%{_mandir}/man8/sepolicy-interface.8*
%{_mandir}/man8/sepolicy-network.8*
%{_mandir}/man8/sepolicy.8*
%{_mandir}/man8/sepolicy-communicate.8*
%{_mandir}/man8/sepolicy-manpage.8*
%{_mandir}/man8/sepolicy-transition.8*
%{bash_completions_dir}/sepolicy

%files -f selinux-python.lang -n python-policycoreutils
%{_sbindir}/semanage
%{_bindir}/chcat
%{_bindir}/audit2allow
%{_bindir}/audit2why
%{_mandir}/man1/audit2allow.1*
%{_mandir}/man1/audit2why.1*
%{_sysconfdir}/dbus-1/system.d/org.selinux.conf
%{_mandir}/man8/chcat.8*
%{_mandir}/man8/semanage*.8*
%{bash_completions_dir}/semanage
%{python3_sitelib}/seobject.py*
#{python3_sitelib}/__pycache__
%{python3_sitelib}/sepolgen
%dir %{python3_sitelib}/sepolicy
%{python3_sitelib}/sepolicy/templates
%dir %{python3_sitelib}/sepolicy/help
%{python3_sitelib}/sepolicy/help/*
%{python3_sitelib}/sepolicy/__init__.py*
%{python3_sitelib}/sepolicy/booleans.py*
%{python3_sitelib}/sepolicy/communicate.py*
%{python3_sitelib}/sepolicy/generate.py*
%{python3_sitelib}/sepolicy/interface.py*
%{python3_sitelib}/sepolicy/manpage.py*
%{python3_sitelib}/sepolicy/network.py*
%{python3_sitelib}/sepolicy/transition.py*
%{python3_sitelib}/sepolicy/sedbus.py*
%{python3_sitelib}/sepolicy*.dist-info/
%{python3_sitelib}/sepolicy/__pycache__

%files dbus
%{_sysconfdir}/dbus-1/system.d/org.selinux.conf
%{_datadir}/dbus-1/system-services/org.selinux.service
%{_datadir}/polkit-1/actions/org.selinux.policy
%{_datadir}/polkit-1/actions/org.selinux.config.policy
%{_datadir}/system-config-selinux/selinux_server.py
%dir %{_datadir}/system-config-selinux/__pycache__
%{_datadir}/system-config-selinux/__pycache__/selinux_server.*

%files -f selinux-gui.lang gui
%{_bindir}/system-config-selinux
%{_bindir}/selinux-polgengui
%{_datadir}/applications/sepolicy.desktop
%{_datadir}/applications/system-config-selinux.desktop
%{_datadir}/applications/selinux-polgengui.desktop
%{_datadir}/icons/hicolor/24x24/apps/system-config-selinux.png
%{_datadir}/pixmaps/system-config-selinux.png
%dir %{_datadir}/system-config-selinux
%dir %{_datadir}/system-config-selinux/__pycache__
%{_datadir}/system-config-selinux/system-config-selinux.png
%{_datadir}/system-config-selinux/*Page.py
%{_datadir}/system-config-selinux/__pycache__/*Page.*
%{_datadir}/system-config-selinux/system-config-selinux.py
%{_datadir}/system-config-selinux/__pycache__/system-config-selinux.*
%{_datadir}/system-config-selinux/*.ui
%{python3_sitelib}/sepolicy/gui.py*
%{python3_sitelib}/sepolicy/sepolicy.glade
%{_datadir}/icons/hicolor/*/apps/sepolicy.png
%{_datadir}/pixmaps/sepolicy.png
%{_mandir}/man8/system-config-selinux.8*
%{_mandir}/man8/selinux-polgengui.8*
%{_mandir}/man8/sepolicy-gui.8*

%files newrole
%attr(0755,root,root) %caps(cap_dac_read_search,cap_setpcap,cap_audit_write,cap_sys_admin,cap_fowner,cap_chown,cap_dac_override=pe) %{_bindir}/newrole
%{_mandir}/man1/newrole.1.gz
%config(noreplace) %{_sysconfdir}/pam.d/newrole

%changelog
%{?autochangelog}
