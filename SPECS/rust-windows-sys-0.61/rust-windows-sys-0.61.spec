# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows-sys
%global full_version 0.61.2
%global pkgname windows-sys-0.61

Name:           rust-windows-sys-0.61
Version:        0.61.2
Release:        %autorelease
Summary:        Rust crate "windows-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:ae137229bcbd6cdf0f7b80a31df61766145077ddf49416a728b02cb3921ff3fc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-link-0.2) >= 0.2.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/docs) = %{version}
Provides:       crate(%{pkgname}/wdk) = %{version}
Provides:       crate(%{pkgname}/wdk-devices) = %{version}
Provides:       crate(%{pkgname}/wdk-devices-bluetooth) = %{version}
Provides:       crate(%{pkgname}/wdk-devices-humaninterfacedevice) = %{version}
Provides:       crate(%{pkgname}/wdk-foundation) = %{version}
Provides:       crate(%{pkgname}/wdk-graphics) = %{version}
Provides:       crate(%{pkgname}/wdk-graphics-direct3d) = %{version}
Provides:       crate(%{pkgname}/wdk-networkmanagement) = %{version}
Provides:       crate(%{pkgname}/wdk-networkmanagement-ndis) = %{version}
Provides:       crate(%{pkgname}/wdk-networkmanagement-windowsfilteringplatform) = %{version}
Provides:       crate(%{pkgname}/wdk-storage) = %{version}
Provides:       crate(%{pkgname}/wdk-storage-filesystem) = %{version}
Provides:       crate(%{pkgname}/wdk-storage-filesystem-minifilters) = %{version}
Provides:       crate(%{pkgname}/wdk-system) = %{version}
Provides:       crate(%{pkgname}/wdk-system-io) = %{version}
Provides:       crate(%{pkgname}/wdk-system-memory) = %{version}
Provides:       crate(%{pkgname}/wdk-system-offlineregistry) = %{version}
Provides:       crate(%{pkgname}/wdk-system-registry) = %{version}
Provides:       crate(%{pkgname}/wdk-system-systeminformation) = %{version}
Provides:       crate(%{pkgname}/wdk-system-systemservices) = %{version}
Provides:       crate(%{pkgname}/wdk-system-threading) = %{version}
Provides:       crate(%{pkgname}/win32) = %{version}
Provides:       crate(%{pkgname}/win32-data) = %{version}
Provides:       crate(%{pkgname}/win32-data-htmlhelp) = %{version}
Provides:       crate(%{pkgname}/win32-data-rightsmanagement) = %{version}
Provides:       crate(%{pkgname}/win32-devices) = %{version}
Provides:       crate(%{pkgname}/win32-devices-alljoyn) = %{version}
Provides:       crate(%{pkgname}/win32-devices-beep) = %{version}
Provides:       crate(%{pkgname}/win32-devices-biometricframework) = %{version}
Provides:       crate(%{pkgname}/win32-devices-bluetooth) = %{version}
Provides:       crate(%{pkgname}/win32-devices-cdrom) = %{version}
Provides:       crate(%{pkgname}/win32-devices-communication) = %{version}
Provides:       crate(%{pkgname}/win32-devices-deviceanddriverinstallation) = %{version}
Provides:       crate(%{pkgname}/win32-devices-devicequery) = %{version}
Provides:       crate(%{pkgname}/win32-devices-display) = %{version}
Provides:       crate(%{pkgname}/win32-devices-dvd) = %{version}
Provides:       crate(%{pkgname}/win32-devices-enumeration) = %{version}
Provides:       crate(%{pkgname}/win32-devices-enumeration-pnp) = %{version}
Provides:       crate(%{pkgname}/win32-devices-fax) = %{version}
Provides:       crate(%{pkgname}/win32-devices-humaninterfacedevice) = %{version}
Provides:       crate(%{pkgname}/win32-devices-nfc) = %{version}
Provides:       crate(%{pkgname}/win32-devices-nfp) = %{version}
Provides:       crate(%{pkgname}/win32-devices-portabledevices) = %{version}
Provides:       crate(%{pkgname}/win32-devices-properties) = %{version}
Provides:       crate(%{pkgname}/win32-devices-pwm) = %{version}
Provides:       crate(%{pkgname}/win32-devices-sensors) = %{version}
Provides:       crate(%{pkgname}/win32-devices-serialcommunication) = %{version}
Provides:       crate(%{pkgname}/win32-devices-tapi) = %{version}
Provides:       crate(%{pkgname}/win32-devices-usb) = %{version}
Provides:       crate(%{pkgname}/win32-devices-webservicesondevices) = %{version}
Provides:       crate(%{pkgname}/win32-foundation) = %{version}
Provides:       crate(%{pkgname}/win32-gaming) = %{version}
Provides:       crate(%{pkgname}/win32-globalization) = %{version}
Provides:       crate(%{pkgname}/win32-graphics) = %{version}
Provides:       crate(%{pkgname}/win32-graphics-dwm) = %{version}
Provides:       crate(%{pkgname}/win32-graphics-gdi) = %{version}
Provides:       crate(%{pkgname}/win32-graphics-gdiplus) = %{version}
Provides:       crate(%{pkgname}/win32-graphics-hlsl) = %{version}
Provides:       crate(%{pkgname}/win32-graphics-opengl) = %{version}
Provides:       crate(%{pkgname}/win32-graphics-printing) = %{version}
Provides:       crate(%{pkgname}/win32-graphics-printing-printticket) = %{version}
Provides:       crate(%{pkgname}/win32-management) = %{version}
Provides:       crate(%{pkgname}/win32-management-mobiledevicemanagementregistration) = %{version}
Provides:       crate(%{pkgname}/win32-media) = %{version}
Provides:       crate(%{pkgname}/win32-media-audio) = %{version}
Provides:       crate(%{pkgname}/win32-media-dxmediaobjects) = %{version}
Provides:       crate(%{pkgname}/win32-media-kernelstreaming) = %{version}
Provides:       crate(%{pkgname}/win32-media-multimedia) = %{version}
Provides:       crate(%{pkgname}/win32-media-streaming) = %{version}
Provides:       crate(%{pkgname}/win32-media-windowsmediaformat) = %{version}
Provides:       crate(%{pkgname}/win32-networking) = %{version}
Provides:       crate(%{pkgname}/win32-networking-activedirectory) = %{version}
Provides:       crate(%{pkgname}/win32-networking-clustering) = %{version}
Provides:       crate(%{pkgname}/win32-networking-httpserver) = %{version}
Provides:       crate(%{pkgname}/win32-networking-ldap) = %{version}
Provides:       crate(%{pkgname}/win32-networking-websocket) = %{version}
Provides:       crate(%{pkgname}/win32-networking-windowswebservices) = %{version}
Provides:       crate(%{pkgname}/win32-networking-winhttp) = %{version}
Provides:       crate(%{pkgname}/win32-networking-wininet) = %{version}
Provides:       crate(%{pkgname}/win32-networking-winsock) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-dhcp) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-dns) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-internetconnectionwizard) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-iphelper) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-multicast) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-ndis) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-netbios) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-netmanagement) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-netshell) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-networkdiagnosticsframework) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-p2p) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-qos) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-rras) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-snmp) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-webdav) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-wifi) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-windowsconnectionmanager) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-windowsfilteringplatform) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-windowsfirewall) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-windowsnetworkvirtualization) = %{version}
Provides:       crate(%{pkgname}/win32-networkmanagement-wnet) = %{version}
Provides:       crate(%{pkgname}/win32-security) = %{version}
Provides:       crate(%{pkgname}/win32-security-applocker) = %{version}
Provides:       crate(%{pkgname}/win32-security-authentication) = %{version}
Provides:       crate(%{pkgname}/win32-security-authentication-identity) = %{version}
Provides:       crate(%{pkgname}/win32-security-authorization) = %{version}
Provides:       crate(%{pkgname}/win32-security-credentials) = %{version}
Provides:       crate(%{pkgname}/win32-security-cryptography) = %{version}
Provides:       crate(%{pkgname}/win32-security-cryptography-catalog) = %{version}
Provides:       crate(%{pkgname}/win32-security-cryptography-certificates) = %{version}
Provides:       crate(%{pkgname}/win32-security-cryptography-sip) = %{version}
Provides:       crate(%{pkgname}/win32-security-cryptography-ui) = %{version}
Provides:       crate(%{pkgname}/win32-security-diagnosticdataquery) = %{version}
Provides:       crate(%{pkgname}/win32-security-directoryservices) = %{version}
Provides:       crate(%{pkgname}/win32-security-enterprisedata) = %{version}
Provides:       crate(%{pkgname}/win32-security-extensibleauthenticationprotocol) = %{version}
Provides:       crate(%{pkgname}/win32-security-isolation) = %{version}
Provides:       crate(%{pkgname}/win32-security-licenseprotection) = %{version}
Provides:       crate(%{pkgname}/win32-security-networkaccessprotection) = %{version}
Provides:       crate(%{pkgname}/win32-security-wintrust) = %{version}
Provides:       crate(%{pkgname}/win32-security-winwlx) = %{version}
Provides:       crate(%{pkgname}/win32-storage) = %{version}
Provides:       crate(%{pkgname}/win32-storage-cabinets) = %{version}
Provides:       crate(%{pkgname}/win32-storage-cloudfilters) = %{version}
Provides:       crate(%{pkgname}/win32-storage-compression) = %{version}
Provides:       crate(%{pkgname}/win32-storage-distributedfilesystem) = %{version}
Provides:       crate(%{pkgname}/win32-storage-filehistory) = %{version}
Provides:       crate(%{pkgname}/win32-storage-filesystem) = %{version}
Provides:       crate(%{pkgname}/win32-storage-imapi) = %{version}
Provides:       crate(%{pkgname}/win32-storage-indexserver) = %{version}
Provides:       crate(%{pkgname}/win32-storage-installablefilesystems) = %{version}
Provides:       crate(%{pkgname}/win32-storage-iscsidisc) = %{version}
Provides:       crate(%{pkgname}/win32-storage-jet) = %{version}
Provides:       crate(%{pkgname}/win32-storage-nvme) = %{version}
Provides:       crate(%{pkgname}/win32-storage-offlinefiles) = %{version}
Provides:       crate(%{pkgname}/win32-storage-operationrecorder) = %{version}
Provides:       crate(%{pkgname}/win32-storage-packaging) = %{version}
Provides:       crate(%{pkgname}/win32-storage-packaging-appx) = %{version}
Provides:       crate(%{pkgname}/win32-storage-projectedfilesystem) = %{version}
Provides:       crate(%{pkgname}/win32-storage-structuredstorage) = %{version}
Provides:       crate(%{pkgname}/win32-storage-vhd) = %{version}
Provides:       crate(%{pkgname}/win32-storage-xps) = %{version}
Provides:       crate(%{pkgname}/win32-system) = %{version}
Provides:       crate(%{pkgname}/win32-system-addressbook) = %{version}
Provides:       crate(%{pkgname}/win32-system-antimalware) = %{version}
Provides:       crate(%{pkgname}/win32-system-applicationinstallationandservicing) = %{version}
Provides:       crate(%{pkgname}/win32-system-applicationverifier) = %{version}
Provides:       crate(%{pkgname}/win32-system-clrhosting) = %{version}
Provides:       crate(%{pkgname}/win32-system-com) = %{version}
Provides:       crate(%{pkgname}/win32-system-com-marshal) = %{version}
Provides:       crate(%{pkgname}/win32-system-com-structuredstorage) = %{version}
Provides:       crate(%{pkgname}/win32-system-com-urlmon) = %{version}
Provides:       crate(%{pkgname}/win32-system-componentservices) = %{version}
Provides:       crate(%{pkgname}/win32-system-console) = %{version}
Provides:       crate(%{pkgname}/win32-system-correlationvector) = %{version}
Provides:       crate(%{pkgname}/win32-system-dataexchange) = %{version}
Provides:       crate(%{pkgname}/win32-system-deploymentservices) = %{version}
Provides:       crate(%{pkgname}/win32-system-developerlicensing) = %{version}
Provides:       crate(%{pkgname}/win32-system-diagnostics) = %{version}
Provides:       crate(%{pkgname}/win32-system-diagnostics-ceip) = %{version}
Provides:       crate(%{pkgname}/win32-system-diagnostics-debug) = %{version}
Provides:       crate(%{pkgname}/win32-system-diagnostics-debug-extensions) = %{version}
Provides:       crate(%{pkgname}/win32-system-diagnostics-etw) = %{version}
Provides:       crate(%{pkgname}/win32-system-diagnostics-processsnapshotting) = %{version}
Provides:       crate(%{pkgname}/win32-system-diagnostics-toolhelp) = %{version}
Provides:       crate(%{pkgname}/win32-system-diagnostics-tracelogging) = %{version}
Provides:       crate(%{pkgname}/win32-system-distributedtransactioncoordinator) = %{version}
Provides:       crate(%{pkgname}/win32-system-environment) = %{version}
Provides:       crate(%{pkgname}/win32-system-errorreporting) = %{version}
Provides:       crate(%{pkgname}/win32-system-eventcollector) = %{version}
Provides:       crate(%{pkgname}/win32-system-eventlog) = %{version}
Provides:       crate(%{pkgname}/win32-system-eventnotificationservice) = %{version}
Provides:       crate(%{pkgname}/win32-system-grouppolicy) = %{version}
Provides:       crate(%{pkgname}/win32-system-hostcompute) = %{version}
Provides:       crate(%{pkgname}/win32-system-hostcomputenetwork) = %{version}
Provides:       crate(%{pkgname}/win32-system-hostcomputesystem) = %{version}
Provides:       crate(%{pkgname}/win32-system-hypervisor) = %{version}
Provides:       crate(%{pkgname}/win32-system-iis) = %{version}
Provides:       crate(%{pkgname}/win32-system-io) = %{version}
Provides:       crate(%{pkgname}/win32-system-ioctl) = %{version}
Provides:       crate(%{pkgname}/win32-system-jobobjects) = %{version}
Provides:       crate(%{pkgname}/win32-system-js) = %{version}
Provides:       crate(%{pkgname}/win32-system-kernel) = %{version}
Provides:       crate(%{pkgname}/win32-system-libraryloader) = %{version}
Provides:       crate(%{pkgname}/win32-system-mailslots) = %{version}
Provides:       crate(%{pkgname}/win32-system-mapi) = %{version}
Provides:       crate(%{pkgname}/win32-system-memory) = %{version}
Provides:       crate(%{pkgname}/win32-system-memory-nonvolatile) = %{version}
Provides:       crate(%{pkgname}/win32-system-messagequeuing) = %{version}
Provides:       crate(%{pkgname}/win32-system-mixedreality) = %{version}
Provides:       crate(%{pkgname}/win32-system-ole) = %{version}
Provides:       crate(%{pkgname}/win32-system-passwordmanagement) = %{version}
Provides:       crate(%{pkgname}/win32-system-performance) = %{version}
Provides:       crate(%{pkgname}/win32-system-performance-hardwarecounterprofiling) = %{version}
Provides:       crate(%{pkgname}/win32-system-pipes) = %{version}
Provides:       crate(%{pkgname}/win32-system-power) = %{version}
Provides:       crate(%{pkgname}/win32-system-processstatus) = %{version}
Provides:       crate(%{pkgname}/win32-system-recovery) = %{version}
Provides:       crate(%{pkgname}/win32-system-registry) = %{version}
Provides:       crate(%{pkgname}/win32-system-remotedesktop) = %{version}
Provides:       crate(%{pkgname}/win32-system-remotemanagement) = %{version}
Provides:       crate(%{pkgname}/win32-system-restartmanager) = %{version}
Provides:       crate(%{pkgname}/win32-system-restore) = %{version}
Provides:       crate(%{pkgname}/win32-system-rpc) = %{version}
Provides:       crate(%{pkgname}/win32-system-search) = %{version}
Provides:       crate(%{pkgname}/win32-system-search-common) = %{version}
Provides:       crate(%{pkgname}/win32-system-securitycenter) = %{version}
Provides:       crate(%{pkgname}/win32-system-services) = %{version}
Provides:       crate(%{pkgname}/win32-system-setupandmigration) = %{version}
Provides:       crate(%{pkgname}/win32-system-shutdown) = %{version}
Provides:       crate(%{pkgname}/win32-system-stationsanddesktops) = %{version}
Provides:       crate(%{pkgname}/win32-system-subsystemforlinux) = %{version}
Provides:       crate(%{pkgname}/win32-system-systeminformation) = %{version}
Provides:       crate(%{pkgname}/win32-system-systemservices) = %{version}
Provides:       crate(%{pkgname}/win32-system-threading) = %{version}
Provides:       crate(%{pkgname}/win32-system-time) = %{version}
Provides:       crate(%{pkgname}/win32-system-tpmbaseservices) = %{version}
Provides:       crate(%{pkgname}/win32-system-useraccesslogging) = %{version}
Provides:       crate(%{pkgname}/win32-system-variant) = %{version}
Provides:       crate(%{pkgname}/win32-system-virtualdosmachines) = %{version}
Provides:       crate(%{pkgname}/win32-system-windowsprogramming) = %{version}
Provides:       crate(%{pkgname}/win32-system-wmi) = %{version}
Provides:       crate(%{pkgname}/win32-ui) = %{version}
Provides:       crate(%{pkgname}/win32-ui-accessibility) = %{version}
Provides:       crate(%{pkgname}/win32-ui-colorsystem) = %{version}
Provides:       crate(%{pkgname}/win32-ui-controls) = %{version}
Provides:       crate(%{pkgname}/win32-ui-controls-dialogs) = %{version}
Provides:       crate(%{pkgname}/win32-ui-hidpi) = %{version}
Provides:       crate(%{pkgname}/win32-ui-input) = %{version}
Provides:       crate(%{pkgname}/win32-ui-input-ime) = %{version}
Provides:       crate(%{pkgname}/win32-ui-input-keyboardandmouse) = %{version}
Provides:       crate(%{pkgname}/win32-ui-input-pointer) = %{version}
Provides:       crate(%{pkgname}/win32-ui-input-touch) = %{version}
Provides:       crate(%{pkgname}/win32-ui-input-xboxcontroller) = %{version}
Provides:       crate(%{pkgname}/win32-ui-interactioncontext) = %{version}
Provides:       crate(%{pkgname}/win32-ui-magnification) = %{version}
Provides:       crate(%{pkgname}/win32-ui-shell) = %{version}
Provides:       crate(%{pkgname}/win32-ui-shell-common) = %{version}
Provides:       crate(%{pkgname}/win32-ui-shell-propertiessystem) = %{version}
Provides:       crate(%{pkgname}/win32-ui-tabletpc) = %{version}
Provides:       crate(%{pkgname}/win32-ui-textservices) = %{version}
Provides:       crate(%{pkgname}/win32-ui-windowsandmessaging) = %{version}
Provides:       crate(%{pkgname}/win32-web) = %{version}
Provides:       crate(%{pkgname}/win32-web-internetexplorer) = %{version}

%description
Source code for takopackized Rust crate "windows-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
