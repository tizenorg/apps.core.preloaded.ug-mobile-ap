%define _usrdir /usr
%define _ugdir  %{_usrdir}/apps/ug-setting-mobileap-efl

Name:		ug-setting-mobileap-efl
Summary:	Tethering UI Gadget Library
Version:	1.0.137
Release:	1
Group:		App/Network
License:	Flora-1.1
Source0:	%{name}-%{version}.tar.gz

%if "%{?profile}" == "wearable"
ExcludeArch: %{arm} %ix86 x86_64
%endif
%if "%{?profile}" == "tv"
ExcludeArch: %{arm} %ix86 x86_64
%endif

BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(elementary)
BuildRequires:	pkgconfig(ui-gadget-1)
BuildRequires:	pkgconfig(capi-network-wifi)
BuildRequires:	pkgconfig(capi-network-tethering)
BuildRequires:	pkgconfig(capi-network-connection)
BuildRequires:	pkgconfig(notification)
BuildRequires:	pkgconfig(efl-extension)
BuildRequires:	cmake
BuildRequires:	edje-bin
BuildRequires:	gettext-tools
Requires(post):	/usr/bin/vconftool

%description
Tethering UI Gadget Library

%prep
%setup -q

%build
cmake -DCMAKE_INSTALL_PREFIX="%{_ugdir}"  \
	.

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install

#License
mkdir -p %{buildroot}%{_datadir}/license
cp LICENSE %{buildroot}%{_datadir}/license/%{name}

%post
/usr/bin/vconftool set -t bool db/private/libug-setting-mobileap-efl/prev_wifi_status 0 -u 5000 -s ug-setting-mobileap-efl
/usr/bin/vconftool set -t int file/private/libug-setting-mobileap-efl/wifi_popup_check_box_status 0 -u 5000 -i -s ug-setting-mobileap-efl
/usr/bin/vconftool set -t int file/private/libug-setting-mobileap-efl/bt_popup_check_box_status 0 -u 5000 -i -s ug-setting-mobileap-efl
/usr/bin/vconftool set -t int file/private/libug-setting-mobileap-efl/usb_popup_check_box_status 0 -u 5000 -i -s ug-setting-mobileap-efl
/usr/bin/vconftool set -t int file/private/libug-setting-mobileap-efl/is_device_rename_local 0 -u 5000 -i -s ug-setting-mobileap-efl
/usr/bin/vconftool set -t int memory/private/libug-setting-mobileap-efl/trying_usb_tethering 0 -u 5000 -i -s ug-setting-mobileap-efl

mkdir -p /usr/apps/ug-setting-mobileap-efl/bin/ -m 777
chown -R 5000:5000 /usr/apps/ug-setting-mobileap-efl/bin/
chsmack -a "_" /usr/apps/ug-setting-mobileap-efl/bin/

%files
%manifest ug-setting-mobileap-efl.manifest
/etc/smack/accesses.d/ug-setting-mobileap-efl.efl
%defattr(-,root,root,-)
/usr/ug/res/locale/*/LC_MESSAGES/ug-setting-mobileap-efl*
/usr/ug/res/images/ug-setting-mobileap-efl/*.png
%{_ugdir}/res/edje/ug-setting-mobileap-efl/*.edj
%{_ugdir}/res/help/ug-setting-mobileap-efl/help_setting_tethering.xml
%{_ugdir}/lib/ug/libug-setting-mobileap-efl.so
/usr/share/packages/ug-setting-mobileap-efl.xml
/usr/apps/ug-setting-mobileap-efl/shared/res/tables/ug-setting-mobileap-efl_ChangeableColorInfo.xml
/usr/apps/ug-setting-mobileap-efl/shared/res/tables/ug-setting-mobileap-efl_fontInfoTable.xml
%{_datadir}/license/%{name}
