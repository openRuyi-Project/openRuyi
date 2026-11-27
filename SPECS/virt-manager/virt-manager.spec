# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           virt-manager
Version:        5.1.0
Release:        %autorelease
Summary:        Desktop tool for managing virtual machines via libvirt
License:        GPL-2.0-or-later
URL:            https://virt-manager.org/
VCS:            git:https://github.com/virt-manager/virt-manager
#!RemoteAsset:  sha256:ccfc44b6c1c0be8398beb687c675d9ea4ca1c721dfb67bd639209a7b0dec11b1
Source:         https://releases.pagure.org/virt-manager/virt-manager-%{version}.tar.xz
BuildSystem:    meson

Patch1:         0001-virtinst-cloudinit-include-empty-meta-data-file.patch

BuildOption(conf):  -Ddefault-hvs="qemu,lxc"
BuildOption(conf):  -Ddefault-graphics=vnc
BuildOption(conf):  -Dupdate-icon-cache=false
BuildOption(conf):  -Dcompile-schemas=false
BuildOption(conf):  -Dtests=disabled

BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  appstream
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-docutils

Requires:       virt-manager-common = %{version}-%{release}
Requires:       python3-gobject
Requires:       gtk3
Requires:       libvirt-glib
# Requires:      gtk-vnc2
Requires:       vte
Requires:       dconf

# Recommends:    gtksourceview4
Recommends:     libvirt-daemon

# Optional inspection of guests
# Suggests:      python3-libguestfs

%description
Virtual Machine Manager provides a graphical tool for administering virtual
machines for KVM, Xen, and LXC. Start, stop, add or remove virtual devices,
connect to a graphical or serial console, and see resource usage statistics
for existing VMs on local or remote machines. Uses libvirt as the backend
management API.

%package        common
Summary:        Common files used by the different Virtual Machine Manager interfaces
Requires:       python3dist(argcomplete)
Requires:       python3dist(libvirt-python)
Requires:       python3-libxml2
Requires:       python3dist(requests)
Requires:       libosinfo
Requires:       python3dist(pygobject)
Requires:       xorriso

%description    common
Common files used by the different virt-manager interfaces, as well as
virt-install related tools.

%package     -n virt-install
Summary:        Utilities for installing virtual machines
Requires:       virt-manager-common = %{version}-%{release}
Requires:       libvirt-client
Provides:       virt-clone
Provides:       virt-xml

%description -n virt-install
Package includes several command line utilities, including virt-install
(build and install new VMs) and virt-clone (clone an existing virtual
machine).

%install -a
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/virt-manager/

rm -rf %{buildroot}%{_datadir}/locale/*@*

%find_lang %{name} --generate-subpackages

%files
%{_bindir}/virt-manager
%{_datadir}/virt-manager/ui
%{_datadir}/virt-manager/virtManager
%{_datadir}/virt-manager/icons
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/virt-manager.desktop
%{_datadir}/glib-2.0/schemas/org.virt-manager.virt-manager.gschema.xml
%{_datadir}/metainfo/virt-manager.appdata.xml
%{_mandir}/man1/virt-manager.1*

%files common -f %{name}.lang
%doc README.md NEWS.md
%license COPYING
%dir %{_datadir}/virt-manager
%{_datadir}/virt-manager/virtinst

%files -n virt-install
%{_bindir}/{virt-install,virt-clone,virt-xml}
%{_datadir}/bash-completion/completions/{virt-install,virt-clone,virt-xml}
%{_mandir}/man1/{virt-install.1*,virt-clone.1*,virt-xml.1*}

%changelog
%autochangelog
